# Generated by Django 3.2.7 on 2021-10-12 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0027_listing_highest_bid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='highest_bid',
            new_name='highest_bidder',
        ),
    ]
