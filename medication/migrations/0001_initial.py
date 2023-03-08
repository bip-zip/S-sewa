# Generated by Django 4.1.6 on 2023-03-08 10:27

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
            name='MedicationSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='institution', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('desc', models.TextField(null=True)),
                ('dose', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MedicineMedicationSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.CharField(max_length=2000, null=True)),
                ('timesaday', models.CharField(choices=[('morning', 'Morning'), ('morning&evening', 'Morning & Evening'), ('morning&afternoon&evening', 'Morning, Afternoon & Evening')], max_length=50)),
                ('emptyStomach', models.BooleanField(default=False)),
                ('medicationSchedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medication.medicationschedule')),
                ('medicine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medication.medicine')),
            ],
        ),
        migrations.AddField(
            model_name='medicationschedule',
            name='medicine',
            field=models.ManyToManyField(related_name='medicine', through='medication.MedicineMedicationSchedule', to='medication.medicine'),
        ),
        migrations.AddField(
            model_name='medicationschedule',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
