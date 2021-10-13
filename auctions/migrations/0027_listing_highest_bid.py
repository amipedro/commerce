# Generated by Django 3.2.7 on 2021-10-12 11:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0026_bid_bid'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='highest_bid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='highest_bidder', to=settings.AUTH_USER_MODEL),
        ),
    ]