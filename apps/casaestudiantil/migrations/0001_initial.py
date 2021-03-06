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
            name='CasaEstudiantil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='nombre')),
            ],
        ),
        migrations.CreateModel(
            name='DescripcionCasa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_dueno', models.CharField(max_length=50, null=True, verbose_name='nombre_dueno')),
                ('capacidad', models.CharField(max_length=5, verbose_name='capacidad')),
                ('camas', models.CharField(max_length=5, verbose_name='camas')),
                ('cuartos', models.CharField(max_length=5, verbose_name='cuartos')),
                ('sillas', models.CharField(max_length=5, verbose_name='sillas')),
                ('cocinas', models.CharField(max_length=5, verbose_name='cocinas')),
                ('banios', models.CharField(max_length=5, verbose_name='banios')),
            ],
        ),
        migrations.AddField(
            model_name='casaestudiantil',
            name='descripcion_casa_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='casaestudiantil.DescripcionCasa'),
        ),
        migrations.AddField(
            model_name='casaestudiantil',
            name='domicilio_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='solicitante.Domicilio'),
        ),
        migrations.AddField(
            model_name='casaestudiantil',
            name='telefono_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='solicitante.Telefono'),
        ),
    ]
