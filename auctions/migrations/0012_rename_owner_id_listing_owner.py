# Generated by Django 3.2.7 on 2021-10-03 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0011_listing_current_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='owner_id',
            new_name='owner',
        ),
    ]
