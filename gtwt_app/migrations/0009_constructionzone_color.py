# Generated by Django 5.1.5 on 2025-04-24 19:23

import gtwt_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gtwt_app', '0008_auto_20250424_1913'),
    ]

    operations = [
        migrations.AddField(
            model_name='constructionzone',
            name='color',
            field=models.CharField(default=gtwt_app.models.generate_random_color, max_length=7),
        ),
    ]
