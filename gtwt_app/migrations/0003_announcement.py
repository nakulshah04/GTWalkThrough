# Generated by Django 4.2.20 on 2025-04-15 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gtwt_app', '0002_constructionzone_submitted_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
