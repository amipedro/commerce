# Generated by Django 3.2.7 on 2021-10-12 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0030_alter_listing_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.TextField(max_length=128),
        ),
    ]
