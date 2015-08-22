# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tco', '0002_result'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food_questions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('input_footprint_shopping_food_meatfisheggs_default', models.FloatField(default=1357.5)),
                ('input_footprint_shopping_food_dairy_default', models.FloatField(default=715)),
                ('input_footprint_shopping_food_fruitvegetables_default', models.FloatField(default=677.5)),
                ('input_footprint_shopping_food_cereals', models.FloatField(default=1672.5)),
                ('input_footprint_shopping_food_otherfood', models.IntegerField(default=1840)),
            ],
        ),
        migrations.CreateModel(
            name='Housing_questions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('input_footprint_housing_electricity_type', models.IntegerField(default=0)),
                ('input_footprint_housing_cleanpercent', models.IntegerField(blank=True)),
                ('input_footprint_housing_naturalgas_type', models.IntegerField(blank=True)),
                ('input_footprint_housing_naturalgas_dollars', models.IntegerField(blank=True)),
                ('input_footprint_housing_heatingoil_type', models.IntegerField(blank=True)),
                ('input_footprint_housing_heatingoil_dollars', models.IntegerField(blank=True)),
                ('input_footprint_housing_heatingoil_gallons', models.IntegerField(blank=True)),
                ('input_footprint_housing_heatingoil_dollars_per_gallon', models.IntegerField(blank=True)),
                ('input_footprint_housing_squarefeet', models.IntegerField(blank=True)),
                ('input_footprint_housing_watersewage', models.FloatField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Shopping_questions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('input_footprint_shopping_goods_type', models.IntegerField(editable=False)),
                ('input_footprint_shopping_goods_total', models.FloatField()),
                ('input_footprint_shopping_services_type', models.IntegerField(editable=False)),
                ('input_footprint_shopping_services_total', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Travel_questions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('input_footprint_transportation_miles1', models.IntegerField()),
                ('input_footprint_transportation_mpg1', models.IntegerField(blank=True)),
                ('input_footprint_transportation_fuel1', models.IntegerField(blank=True)),
                ('input_footprint_transportation_miles2', models.IntegerField()),
                ('input_footprint_transportation_mpg2', models.IntegerField(blank=True)),
                ('input_footprint_transportation_fuel2', models.IntegerField(blank=True)),
                ('input_footprint_transportation_publictrans', models.IntegerField(blank=True)),
                ('input_footprint_transportation_airtotal', models.IntegerField(blank=True)),
            ],
        ),
    ]
