# Generated by Django 3.2.7 on 2021-10-10 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0022_rename_highest_bidder_id_bid_bidder_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bid',
            name='highest_bid',
        ),
    ]
