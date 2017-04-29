# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.OneToOneField(serialize=False, primary_key=True, to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(max_length=100)),
                ('visible', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.OneToOneField(serialize=False, primary_key=True, to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('main_category', models.CharField(max_length=50)),
                ('categories', models.TextField()),
                ('shop_level', models.IntegerField()),
                ('is_in_lottery', models.BooleanField(default=False)),
                ('date_of_creation', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_of_update', models.DateTimeField(null=True, blank=True)),
            ],
        ),
    ]
