# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20170429_1306'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='logo',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]
