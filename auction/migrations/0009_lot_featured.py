# Generated by Django 3.0 on 2019-12-31 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0008_auction_winning_bid'),
    ]

    operations = [
        migrations.AddField(
            model_name='lot',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]
