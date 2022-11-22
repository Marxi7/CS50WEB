# Generated by Django 4.1 on 2022-09-03 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_remove_listings_bids_listings_bids'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listings',
            name='bids',
        ),
        migrations.AddField(
            model_name='listings',
            name='bids',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='listing_bids', to='auctions.bids'),
        ),
    ]