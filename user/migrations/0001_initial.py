# Generated by Django 4.0.2 on 2022-02-16 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('firebase_uid', models.CharField(max_length=28, primary_key=True, serialize=False)),
                ('google_id', models.EmailField(max_length=254)),
                ('google_profile_image', models.EmailField(max_length=254)),
                ('google_name', models.CharField(max_length=40)),
                ('app_name', models.CharField(max_length=40)),
                ('latitude', models.FloatField(db_index=True)),
                ('longitude', models.FloatField(db_index=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]