# Generated by Django 3.0 on 2019-12-31 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0007_auction_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='winning_bid',
            field=models.IntegerField(default=0),
        ),
    ]
