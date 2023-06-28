# Generated by Django 4.2.1 on 2023-06-23 18:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0009_alter_images_post_alter_post_somd'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='scrap',
            field=models.ManyToManyField(blank=True, related_name='scrap', to=settings.AUTH_USER_MODEL),
        ),
    ]