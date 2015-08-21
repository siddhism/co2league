# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tco', '0003_food_question_housing_questions_shopping_questions_travel_questions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='housing_questions',
            name='input_footprint_housing_electricity_type',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='shopping_questions',
            name='input_footprint_shopping_goods_type',
            field=models.IntegerField(),
        ),
    ]
