# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2020-02-25 18:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("studies", "0061_response_is_preview")]

    operations = [
        migrations.AddField(
            model_name="study",
            name="shared_preview",
            field=models.BooleanField(default=False),
        )
    ]