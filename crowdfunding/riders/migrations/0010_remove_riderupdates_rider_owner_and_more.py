# Generated by Django 4.2.3 on 2023-09-08 06:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('riders', '0009_remove_rider_kms_ridden'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='riderupdates',
            name='rider_owner',
        ),
        migrations.AddField(
            model_name='riderupdates',
            name='rider_posting',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='updates', to='riders.rider'),
            preserve_default=False,
        ),
    ]
