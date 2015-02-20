# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stepupmountains', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='climbingobject',
            old_name='object_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='mountain',
            old_name='mountain_comment',
            new_name='comment',
        ),
        migrations.RenameField(
            model_name='mountain',
            old_name='mountain_elevation',
            new_name='elevation',
        ),
        migrations.RenameField(
            model_name='mountain',
            old_name='mountain_name',
            new_name='name',
        ),
    ]
