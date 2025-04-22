from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User


class ConstructionZone(models.Model):
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    coordinates = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.description[:30]} ({self.start_date} to {self.end_date})"

@admin.register(ConstructionZone)
class ConstructionZoneAdmin(admin.ModelAdmin):
    list_display = ("description", "start_date", "end_date", "created_at", "is_verified", "submitted_by")
    list_filter = ("start_date", "end_date", "is_verified")
    search_fields = ("description", "submitted_by__username")
    list_editable = ("is_verified",)
    readonly_fields = ("created_at", "submitted_by")
    save_on_top = True

class SavedRoute(models.Model):
    user          = models.ForeignKey(User, on_delete=models.CASCADE, related_name='saved_routes')
    name          = models.CharField(max_length=100)
    origin        = models.CharField(max_length=255)
    destination   = models.CharField(max_length=255)
    travel_mode   = models.CharField(max_length=20)       # e.g. WALKING, DRIVING, BICYCLING
    steps         = models.JSONField()                    # store the entire directions JSON if you want
    distance_text = models.CharField(max_length=50)       # e.g. "2.3 mi"
    duration_text = models.CharField(max_length=50)       # e.g. "12 mins"
    created_at    = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.origin} → {self.destination})"