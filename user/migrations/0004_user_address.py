# Generated by Django 4.0.2 on 2022-02-20 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_user_google_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(default='82, Eunbong-ro, Namdong-gu, Incheon, Republic of Korea', max_length=100),
        ),
    ]