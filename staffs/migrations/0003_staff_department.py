# Generated by Django 3.0.5 on 2020-04-25 20:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('camp', '0001_initial'),
        ('staffs', '0002_staff_postscript'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='camp.Department'),
        ),
    ]
