# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-24 12:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='street_address1',
            new_name='address_line1',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='street_address2',
            new_name='address_line2',
        ),
        migrations.RemoveField(
            model_name='order',
            name='phone_number',
        ),
    ]
