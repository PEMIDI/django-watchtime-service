# Generated by Django 3.2 on 2024-05-11 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_rename_total_watch_time_watchtime_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchtime',
            name='last_moment',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
