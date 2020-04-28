# Generated by Django 3.0.5 on 2020-04-28 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('camp', '0001_initial'),
        ('personal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Camper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(max_length=255)),
                ('parent_phone', models.CharField(max_length=10)),
                ('parent_name', models.CharField(max_length=255)),
                ('group', models.CharField(max_length=255, null=True)),
                ('camp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='camp.Camp')),
                ('personal', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='personal.Personal')),
            ],
        ),
    ]
