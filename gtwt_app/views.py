from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import ConstructionZone
from .models import SavedRoute
from django.contrib.auth.forms import UserCreationForm
from datetime import datetime
from datetime import date
import json
from django.utils.safestring import mark_safe
from django.core.serializers.json import DjangoJSONEncoder
from django.views.decorators.http import require_POST
from .models import SavedRoute

def home(request):
    if request.user.is_authenticated:
        today = date.today()
        upcoming_zones = (
            ConstructionZone.objects
            .filter(start_date__gt=today)
            .order_by('start_date')[:3]
        )
        return render(request, 'home.html', {
          'upcoming_zones': upcoming_zones
        })
    else:
        return render(request, 'about.html')  

# About View
def about(request):
    return render(request, 'about.html')

# Register View
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']

# Register View
def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created. Please log in.')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'Auth/register.html', {'form': form})

# Login View
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'Auth/login.html', {'form': form})

# Logout View
def logout_view(request):
    logout(request)
    return redirect('login')

# === Construction Zone Views ===

@login_required
def map_view(request):
    return render(request, "map.html")

@csrf_exempt
@login_required
def submit_zone(request):
    if request.method == "POST":
        coords = request.POST.get("coordinates")
        description = request.POST.get("description")
        start = request.POST.get("start_date")
        end = request.POST.get("end_date")
        ConstructionZone.objects.create(
            submitted_by=request.user,
            coordinates=coords,
            description=description,
            start_date=start,
            end_date=end
        )
        return JsonResponse({"success": True})

@staff_member_required
def admin_zones(request):
    zones = ConstructionZone.objects.all()
    return render(request, "admin_zones.html", {"zones": zones})

@staff_member_required
def verify_zone(request, zone_id):
    zone = get_object_or_404(ConstructionZone, id=zone_id)
    zone.is_verified = True
    zone.save()
    return redirect("admin_zones")

@staff_member_required
def delete_zone(request, zone_id):
    zone = get_object_or_404(ConstructionZone, id=zone_id)
    zone.delete()
    return redirect("admin_zones")

@csrf_exempt
@login_required
def save_zone(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        ConstructionZone.objects.create(
            submitted_by=request.user,
            description=data['description'],
            start_date=datetime.strptime(data['start_date'], '%Y-%m-%d'),
            end_date=datetime.strptime(data['end_date'], '%Y-%m-%d'),
            coordinates=data['coordinates'],
        )
        return JsonResponse({'status': 'success'})
    return JsonResponse({'error': 'POST required'}, status=400)


def get_zones(request):
    zones = ConstructionZone.objects.all().values()
    return JsonResponse(list(zones), safe=False)


@login_required
def my_reports(request):
    user_zones = ConstructionZone.objects.filter(submitted_by=request.user).order_by('-created_at')

    zone_data = [
        {
            "id": zone.id,  
            "description": zone.description,
            "start_date": zone.start_date.strftime("%Y-%m-%d"),
            "end_date": zone.end_date.strftime("%Y-%m-%d"),
            "coordinates": zone.coordinates,
        }
        for zone in user_zones
    ]

    return render(request, 'my_reports.html', {
        'zones': mark_safe(json.dumps(zone_data, cls=DjangoJSONEncoder))
    })

@csrf_exempt
@require_POST
@login_required
def delete_zone(request):
    try:
        data = json.loads(request.body)
        zone_id = data.get("id")
        zone = ConstructionZone.objects.get(id=zone_id, submitted_by=request.user)
        zone.delete()
        return JsonResponse({"success": True})
    except ConstructionZone.DoesNotExist:
        return JsonResponse({"success": False, "error": "Zone not found"}, status=404)
    

@login_required
@require_POST
def save_route(request):
    data = json.loads(request.body)
    route = SavedRoute.objects.create(
        user          = request.user,
        name          = data.get('name') or f"{data['origin']} → {data['destination']}",
        origin        = data['origin'],
        destination   = data['destination'],
        travel_mode   = data['mode'],
        steps         = data['steps'],
        distance_text = data['distance'],
        duration_text = data['duration']
    )
    return JsonResponse({'success': True, 'id': route.id})

@login_required
def my_routes(request):
    routes = SavedRoute.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'my_routes.html', {'routes': routes})

# Rename a saved route
@csrf_exempt
def rename_route(request):
    if request.method == "POST":
        data = json.loads(request.body)
        route_id = data.get("id")
        new_name = data.get("name")
        try:
            route = SavedRoute.objects.get(id=route_id, user=request.user)
            route.name = new_name
            route.save()
            return JsonResponse({"success": True})
        except SavedRoute.DoesNotExist:
            return JsonResponse({"success": False, "error": "Not found"}, status=404)
    return JsonResponse({"success": False, "error": "Invalid request"}, status=400)

@csrf_exempt
def delete_route(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            route_id = data.get("id")

            route = SavedRoute.objects.get(id=route_id, user=request.user)
            route.delete()
            return JsonResponse({"success": True})

        except SavedRoute.DoesNotExist:
            return JsonResponse({"error": "Route not found."}, status=404)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request."}, status=400)