# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('stepupmountains', '0002_auto_20150207_2234'),
    ]

    operations = [
        migrations.AddField(
            model_name='climbed',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime.now),
            preserve_default=True,
        ),
    ]
