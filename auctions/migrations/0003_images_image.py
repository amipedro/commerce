# Generated by Django 3.2.7 on 2021-09-30 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_rename_creator_id_id_listing_creator_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
