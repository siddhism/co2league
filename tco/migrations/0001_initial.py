# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('input_location', models.CharField(max_length=5)),
                ('input_income', models.CharField(max_length=20, choices=[(b'1', b'Average'), (b'2', b'Less than $10,000'), (b'3', b'$10,000 to $19,999'), (b'4', b'$20,000 to $29,999'), (b'5', b'$30,000 to $39,999'), (b'6', b'$40,000 to $49,999'), (b'7', b'$50,000 to $59,999'), (b'8', b'$60,000 to $79,999'), (b'9', b'$80,000 to $99,999'), (b'10', b'$100,000 to $119,999'), (b'11', b'$120,000 or more')])),
                ('input_location_mode', models.CharField(max_length=10, choices=[(b'1', b'ZIP code'), (b'2', b'City'), (b'3', b'County'), (b'4', b'State')])),
                ('input_size', models.CharField(max_length=10, choices=[(b'0', b'Average'), (b'1', b'1 person'), (b'2', b'2 person'), (b'3', b'3 person'), (b'4', b'4 person'), (b'5', b'5 person')])),
            ],
        ),
    ]
