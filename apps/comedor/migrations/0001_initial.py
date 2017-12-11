# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-07 20:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('solicitante', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='nombre')),
                ('domicilio_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='solicitante.Domicilio')),
                ('telefono_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='solicitante.Telefono')),
            ],
        ),
    ]
