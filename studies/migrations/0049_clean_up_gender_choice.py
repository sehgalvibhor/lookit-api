# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-07-12 21:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("studies", "0048_change_include_to_required")]

    operations = [
        migrations.AlterField(
            model_name="eligibleparticipantquerymodel",
            name="gender_specification",
            field=models.PositiveSmallIntegerField(
                choices=[(0, "Not answered"), (1, "Other"), (2, "Male"), (3, "Female")],
                null=True,
            ),
        )
    ]
