# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('careers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='career',
            name='code',
            field=models.CharField(max_length=10),
        ),
    ]
