# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-04 14:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='staff',
            options={'permissions': [('schedule_appointment', 'Can schedule appointments'), ('write_prescription', 'Can write prescriptions')], 'verbose_name': 'Staff', 'verbose_name_plural': 'Staff'},
        ),
    ]