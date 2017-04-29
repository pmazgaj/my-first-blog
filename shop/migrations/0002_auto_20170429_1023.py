# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='id',
            field=models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False),
        ),
    ]
