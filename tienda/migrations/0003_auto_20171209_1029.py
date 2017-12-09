# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0002_auto_20171209_0954'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compra',
            name='codigo',
        ),
        migrations.AddField(
            model_name='compra',
            name='fecha_compra',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
