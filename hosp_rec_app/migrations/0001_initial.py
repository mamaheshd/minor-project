# Generated by Django 4.0.4 on 2023-03-09 22:59

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('hosId', models.IntegerField(primary_key=True, serialize=False)),
                ('hosName', models.CharField(max_length=50)),
                ('address', models.CharField(blank=True, max_length=50, null=True)),
                ('hosImage', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('hosLat', models.FloatField()),
                ('hosLong', models.FloatField()),
                ('hosType', models.CharField(choices=[('Government', 'Government'), ('Private', 'Private')], max_length=50)),
                ('hosSpec', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('Orthopedics', 'Orthopedics'), ('Cardiology', 'Cardiology'), ('Neurology', 'Neurology'), ('Oncology', 'Oncology'), ('Pediatrics', 'Pediatrics'), ('Dermatology', 'Dermatology'), ('Gastroenterology', 'Gastroenterology'), ('Gynecology', 'Gynecology'), ('Psychiatry', 'Psychiatry'), ('Ophthalmology', 'Ophthalmology'), ('Pulmonology', 'Pulmonology'), ('Nephrology', 'Nephrology')], max_length=50), size=None)),
            ],
        ),
        migrations.CreateModel(
            name='UserResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('details', models.CharField(blank=True, max_length=100, null=True)),
                ('hosp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hosp_rec_app.hospital')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Preference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preferred_hosp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hosp_rec_app.hospital')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]