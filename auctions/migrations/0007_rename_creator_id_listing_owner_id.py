# Generated by Django 3.2.7 on 2021-10-01 22:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_auto_20211001_1919'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='creator_id',
            new_name='owner_id',
        ),
    ]