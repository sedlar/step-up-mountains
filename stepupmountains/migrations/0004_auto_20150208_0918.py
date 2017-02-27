# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('stepupmountains', '0003_climbed_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='climbed',
            name='datetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
