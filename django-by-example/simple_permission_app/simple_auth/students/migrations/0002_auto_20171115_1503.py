# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-15 07:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'permissions': (('views_student_list', '查看学员信息表'), ('views_student_info', '查看学员详细信息'))},
        ),
    ]
