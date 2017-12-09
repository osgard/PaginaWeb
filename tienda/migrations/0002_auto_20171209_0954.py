# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='infor',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='compra',
            name='clienteC',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
