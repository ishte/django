# Generated by Django 4.0.6 on 2022-07-13 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tkiapp', '0003_remove_projecttracker_project_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projecttracker',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
