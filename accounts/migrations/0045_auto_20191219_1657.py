# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-12-19 21:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("accounts", "0044_new-analytics-permissions")]

    operations = [
        migrations.AlterField(
            model_name="demographicdata",
            name="age",
            field=models.CharField(
                blank=True,
                choices=[
                    ("<18", "under 18"),
                    ("18-21", "18-21"),
                    ("22-24", "22-24"),
                    ("25-29", "25-29"),
                    ("30-34", "30-34"),
                    ("35-39", "35-39"),
                    ("40-44", "40-44"),
                    ("45-49", "45-49"),
                    ("50s", "50-59"),
                    ("60s", "60-69"),
                    (">70", "70 or over"),
                ],
                max_length=5,
            ),
        )
    ]
