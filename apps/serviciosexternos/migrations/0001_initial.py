# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-09 07:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServiciosExternos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField(max_length=250)),
                ('tipo', models.CharField(choices=[('BECA', 'BECA'), ('SERVICIO', 'SERVICIO'), ('OTRO', 'OTRO')], max_length=50)),
                ('organizacion', models.CharField(choices=[('BECA', 'BECA'), ('SEE', 'SEE'), ('INCUFIDEZ', 'INCUFIDEZ'), ('CEISPD', 'CEISPD'), ('DIF', 'DIF'), ('CAVIZ', 'CAVIZ'), ('VIFAC', 'VIFAC'), ('IJEZ', 'IJEZ'), ('INMUZA', 'INMUZA'), ('OTRO', 'OTRO')], max_length=50)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
