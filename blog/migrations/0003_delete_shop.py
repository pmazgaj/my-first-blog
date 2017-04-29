# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_shop'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Shop',
        ),
    ]
