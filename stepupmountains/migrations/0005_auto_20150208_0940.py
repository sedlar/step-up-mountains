# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stepupmountains', '0004_auto_20150208_0918'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Climbed',
            new_name='Climb',
        ),
    ]
