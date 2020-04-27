# Generated by Django 3.0.5 on 2020-04-25 12:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Camp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('desc', models.TextField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('logo', models.ImageField(upload_to='logo/')),
                ('head', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('typeOfMC', models.CharField(max_length=255)),
                ('desc', models.TextField()),
                ('camp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='camp.Camp')),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('typeOfDepartment', models.CharField(max_length=255)),
                ('desc', models.TextField()),
                ('camp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='camp.Camp')),
            ],
        ),
    ]
