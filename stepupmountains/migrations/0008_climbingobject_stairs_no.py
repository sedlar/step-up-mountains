# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stepupmountains', '0007_auto_20150225_1957'),
    ]

    operations = [
        migrations.AddField(
            model_name='climbingobject',
            name='stairs_no',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
