# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stepupmountains', '0005_auto_20150208_0940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='climbingobject',
            name='height',
            field=models.FloatField(),
            preserve_default=True,
        ),
    ]
