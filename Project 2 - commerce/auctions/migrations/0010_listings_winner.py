# Generated by Django 4.1 on 2022-09-03 17:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_remove_listings_bids_bids_listing'),
    ]

    operations = [
        migrations.AddField(
            model_name='listings',
            name='winner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='winner_listing', to=settings.AUTH_USER_MODEL),
        ),
    ]