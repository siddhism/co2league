# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tco', '0004_auto_20150821_1026'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Food_question',
            new_name='Food_questions',
        ),
    ]
