# Generated by Django 3.0.3 on 2020-04-22 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EAD_app', '0017_auto_20200422_1749'),
    ]

    operations = [
        migrations.RenameField(
            model_name='venue',
            old_name='requested_venue',
            new_name='requested_venue_secy',
        ),
        migrations.RemoveField(
            model_name='venue',
            name='booked_by',
        ),
        migrations.AddField(
            model_name='venue',
            name='event_name',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='venue',
            name='requested_venue_student',
            field=models.CharField(choices=[('303', 'lab-303'), ('306', 'lab-306'), ('307', 'lab-307')], max_length=20, null=True),
        ),
    ]
