from django.db import models
from django.contrib.auth.models import User

class ConstructionZone(models.Model):
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    coordinates = models.JSONField()  # Stores list of lat/lng points
    start_date = models.DateField()
    end_date = models.DateField()
    is_verified = models.BooleanField(default=False)
    submitted_at = models.DateTimeField(auto_now_add=True)