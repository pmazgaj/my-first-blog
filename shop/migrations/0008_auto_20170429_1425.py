# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20170429_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='date_of_creation',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='shop',
            name='date_of_update',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2017, 4, 29, 12, 25, 47, 969299, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='shop',
            name='logo',
            field=models.ImageField(verbose_name='', upload_to=''),
        ),
    ]
