# Generated by Django 4.1.6 on 2023-03-08 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='full_name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
