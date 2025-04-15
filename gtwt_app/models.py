from django.db import models
from django.contrib import admin

class ConstructionZone(models.Model):
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    coordinates = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.description[:30]} ({self.start_date} to {self.end_date})"

@admin.register(ConstructionZone)
class ConstructionZoneAdmin(admin.ModelAdmin):
    list_display = ("description", "start_date", "end_date", "created_at")
    search_fields = ("description",)
    list_filter = ("start_date", "end_date")