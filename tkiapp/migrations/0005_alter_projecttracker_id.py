# Generated by Django 4.0.6 on 2022-07-13 12:08

from django.db import migrations, models
import tkiapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('tkiapp', '0004_alter_projecttracker_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projecttracker',
            name='id',
            field=models.CharField(default=tkiapp.models.project_tracker_generate_id, max_length=10, primary_key=True, serialize=False),
        ),
    ]
