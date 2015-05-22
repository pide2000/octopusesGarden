# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restDataProvider', '0003_auto_20150520_2217'),
    ]

    operations = [
        migrations.AddField(
            model_name='pointofinterest',
            name='mapsLink',
            field=models.URLField(null=True),
        ),
    ]
