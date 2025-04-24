from django.db import migrations
import random

def assign_fresh_colors(apps, schema_editor):
    ConstructionZone = apps.get_model('gtwt_app', 'ConstructionZone')
    for zone in ConstructionZone.objects.all():
        zone.color = '#' + ''.join(random.choices('0123456789ABCDEF', k=6))
        zone.save()

class Migration(migrations.Migration):

    dependencies = [
        ('gtwt_app', '0006_constructionzone_is_verified'),  # replace with your last migration name
    ]

    operations = [
        migrations.RunPython(assign_fresh_colors),
    ]