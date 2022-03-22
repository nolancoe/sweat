# Generated by Django 2.2.15 on 2022-03-22 15:37

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0002_auto_20220322_1532'),
    ]

    operations = [
        migrations.AddField(
            model_name='privatechatroom',
            name='connected_users',
            field=models.ManyToManyField(blank=True, related_name='connected_users', to=settings.AUTH_USER_MODEL),
        ),
    ]
