# Generated by Django 3.0.5 on 2020-04-27 22:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
        ('flow', '0004_auto_20200427_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flow',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='locations.Location'),
        ),
    ]
