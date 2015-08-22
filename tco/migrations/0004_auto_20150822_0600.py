# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tco', '0003_food_questions_housing_questions_shopping_questions_travel_questions'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='input_footprint_housing_squarefeet',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='questions',
            name='input_footprint_shopping_goods_total',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='questions',
            name='input_footprint_shopping_services_total',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='questions',
            name='input_footprint_transportation_airtotal',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='questions',
            name='input_footprint_transportation_publictrans',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='shopping_questions',
            name='input_footprint_shopping_goods_type',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='shopping_questions',
            name='input_footprint_shopping_services_type',
            field=models.IntegerField(),
        ),
    ]
