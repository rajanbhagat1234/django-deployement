# Generated by Django 3.0.3 on 2020-04-22 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EAD_app', '0023_auto_20200423_0155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_info',
            name='role',
            field=models.CharField(default='student', max_length=30),
        ),
    ]