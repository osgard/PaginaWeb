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
            name='Artista',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nombreA', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('total', models.FloatField(blank=True, null=True)),
                ('cantidad', models.FloatField(blank=True, null=True)),
                ('codigo', models.CharField(max_length=30, blank=True, null=True)),
                ('clienteC', models.ForeignKey(to='tienda.Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Disquera',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nombreD', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nombreG', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nombreP', models.CharField(max_length=30)),
                ('precio', models.FloatField()),
                ('portada', models.ImageField(blank=True, null=True, upload_to='galeria')),
                ('stock', models.IntegerField(blank=True, null=True)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('artista', models.ForeignKey(to='tienda.Artista')),
                ('disquera', models.ForeignKey(to='tienda.Disquera')),
                ('genero', models.ForeignKey(to='tienda.Genero')),
            ],
        ),
        migrations.AddField(
            model_name='compra',
            name='productoC',
            field=models.ForeignKey(to='tienda.Producto'),
        ),
    ]
