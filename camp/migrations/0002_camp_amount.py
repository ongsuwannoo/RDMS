# Generated by Django 3.0.5 on 2020-04-29 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='camp',
            name='amount',
            field=models.IntegerField(default=0, null=True),
        ),
    ]