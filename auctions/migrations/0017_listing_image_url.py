# Generated by Django 3.2.7 on 2021-10-06 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0016_delete_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='image_url',
            field=models.CharField(default=1, max_length=256),
            preserve_default=False,
        ),
    ]