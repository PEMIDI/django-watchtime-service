# Generated by Django 3.2 on 2024-05-11 03:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_alter_watchtime_total_watch_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='watchtime',
            old_name='total_watch_time',
            new_name='total',
        ),
    ]
