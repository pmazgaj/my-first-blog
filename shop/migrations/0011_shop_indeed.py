# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-03 13:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_shop_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='indeed',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
