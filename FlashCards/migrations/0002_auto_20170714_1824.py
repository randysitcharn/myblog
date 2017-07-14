# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FlashCards', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deck',
            name='desc',
            field=models.CharField(max_length='255'),
        ),
        migrations.AlterField(
            model_name='deck',
            name='img_alt',
            field=models.CharField(max_length='255'),
        ),
    ]
