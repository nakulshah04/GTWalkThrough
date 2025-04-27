import random
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

def generate_random_color():
    return '#' + ''.join(random.choices('0123456789ABCDEF', k=6))

class ConstructionZone(models.Model):
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    coordinates = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    color = models.CharField(max_length=7, default=generate_random_color)

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
    travel_mode   = models.CharField(max_length=20)
    steps         = models.JSONField()
    distance_text = models.CharField(max_length=50)
    duration_text = models.CharField(max_length=50)
    created_at    = models.DateTimeField(auto_now_add=True)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} ({self.origin} → {self.destination})"
    
class Announcement(models.Model):
    title = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    from django.contrib import admin

@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',)
    ordering = ('-created_at',)

        

