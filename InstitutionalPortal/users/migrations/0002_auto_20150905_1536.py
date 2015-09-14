# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Administrator',
            fields=[
            ],
            options={
                'verbose_name': 'Administrator',
                'proxy': True,
                'verbose_name_plural': 'Administrators',
            },
            bases=('users.user',),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
            ],
            options={
                'verbose_name': 'Student',
                'proxy': True,
                'verbose_name_plural': 'Students',
            },
            bases=('users.user',),
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
            ],
            options={
                'verbose_name': 'Teacher',
                'proxy': True,
                'verbose_name_plural': 'Teachers',
            },
            bases=('users.user',),
        ),
        migrations.CreateModel(
            name='TeacherAdministrator',
            fields=[
            ],
            options={
                'verbose_name': 'TeacherAdministrator',
                'proxy': True,
                'verbose_name_plural': 'TeachersAdministrators',
            },
            bases=('users.user',),
        ),
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='type',
            field=models.CharField(max_length=1, default='s', choices=[('s', 'Students'), ('t', 'Teachers'), ('a', 'Admin_personal'), ('b', 'Teachers_and_admin_personal')]),
        ),
    ]
