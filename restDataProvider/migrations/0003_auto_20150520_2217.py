# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restDataProvider', '0002_auto_20150520_2214'),
    ]

    operations = [
        migrations.AddField(
            model_name='pointofinterest',
            name='deleted',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='pointofinterest',
            name='rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='pointofinterest',
            name='description',
            field=models.CharField(max_length=500),
        ),
    ]
