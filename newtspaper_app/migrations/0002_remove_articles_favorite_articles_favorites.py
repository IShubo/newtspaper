# Generated by Django 4.1.3 on 2022-12-11 19:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('newtspaper_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles',
            name='favorite',
        ),
        migrations.AddField(
            model_name='articles',
            name='favorites',
            field=models.ManyToManyField(blank=True, default=None, related_name='favorite', to=settings.AUTH_USER_MODEL),
        ),
    ]
