# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Debt',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('year', models.DateField()),
                ('semester', models.SmallIntegerField(choices=[(1, 'semester1'), (2, 'semester2')], default=1)),
                ('inscription_payment', models.DecimalField(max_digits=15, default=0.0, decimal_places=2)),
                ('library_debts', models.DecimalField(max_digits=15, default=0.0, decimal_places=2)),
                ('laboratory_debts', models.DecimalField(max_digits=15, default=0.0, decimal_places=2)),
                ('username', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
