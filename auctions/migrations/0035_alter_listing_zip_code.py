# Generated by Django 3.2.7 on 2021-10-12 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0034_comment_comment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='zip_code',
            field=models.IntegerField(default=''),
        ),
    ]
