# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-06-29 03:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cant_insumos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Cant_personas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Insumo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('descripcion', models.CharField(blank=True, max_length=40)),
                ('stock', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reservacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('hora_inicio', models.TimeField()),
                ('hora_termino', models.TimeField()),
                ('capacidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rooms.Cant_personas')),
                ('insumos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rooms.Cant_insumos')),
            ],
        ),
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('ubicacion', models.CharField(blank=True, max_length=20)),
                ('horario_disp', models.CharField(max_length=30)),
                ('estado', models.CharField(blank=True, max_length=20)),
                ('capacidad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rooms.Cant_personas')),
                ('insumos', models.ManyToManyField(to='rooms.Insumo')),
            ],
        ),
        migrations.AddField(
            model_name='reservacion',
            name='sala',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rooms.Sala'),
        ),
        migrations.AddField(
            model_name='reservacion',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
