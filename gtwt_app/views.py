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

# Home view
def home(request):
    return render(request, 'home.html')

# About View
def about(request):
    return render(request, 'about.html')

# Register View
class CustomUserCreationForm(forms.ModelForm):
    # ... your existing form definition here ...
    # (left unchanged for brevity)
    pass  # remove this line in actual code

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