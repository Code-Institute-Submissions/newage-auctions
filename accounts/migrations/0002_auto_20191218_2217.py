# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-12-18 22:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdetails',
            old_name='post_code',
            new_name='postcode',
        ),
    ]
