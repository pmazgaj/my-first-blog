# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import shop.models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_shop_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='logo',
            field=models.ImageField(upload_to=shop.models.user_directory_path),
        ),
    ]
