# Generated by Django 3.0.3 on 2020-04-22 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EAD_app', '0016_auto_20200422_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_info',
            name='role',
            field=models.CharField(choices=[('student', 'Student'), ('None', 'none')], max_length=10),
        ),
        migrations.AlterField(
            model_name='venue',
            name='requested_venue',
            field=models.CharField(choices=[('l26', 'LH-16'), ('audi', 'Auditorium'), ('arena', 'Audi Arena')], max_length=20),
        ),
    ]
