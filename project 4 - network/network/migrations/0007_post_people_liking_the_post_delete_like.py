# Generated by Django 4.1 on 2022-09-13 15:03

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0006_alter_post_imageurl'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='people_liking_the_post',
            field=models.ManyToManyField(blank=True, related_name='people_liking', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]
