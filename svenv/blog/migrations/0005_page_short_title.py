# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='short_title',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
