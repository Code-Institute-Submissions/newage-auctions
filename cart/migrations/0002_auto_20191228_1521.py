# Generated by Django 3.0 on 2019-12-28 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0006_auction_winner'),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='auction',
        ),
        migrations.AddField(
            model_name='cart',
            name='auction',
            field=models.ManyToManyField(blank=True, to='auction.Auction'),
        ),
    ]
