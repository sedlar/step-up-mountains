# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stepupmountains', '0006_auto_20150222_2118'),
    ]

    operations = [
        migrations.AddField(
            model_name='climbingobject',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='climbingobject',
            name='order',
            field=models.IntegerField(default=0),
        ),
    ]
