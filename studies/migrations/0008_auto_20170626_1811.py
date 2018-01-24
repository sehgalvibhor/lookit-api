# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-26 18:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studies', '0007_auto_20170626_1504'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='study',
            options={'permissions': (('can_view_study', 'Can View Study'), ('can_create_study', 'Can Create Study'), ('can_edit_study', 'Can Edit Study'), ('can_remove_study', 'Can Remove Study'), ('can_activate_study', 'Can Activate Study'), ('can_deactivate_study', 'Can Deactivate Study'), ('can_pause_study', 'Can Pause Study'), ('can_resume_study', 'Can Resume Study'), ('can_approve_study', 'Can Approve Study'), ('can_submit_study', 'Can Submit Study'), ('can_retract_study', 'Can Retract Study'), ('can_resubmit_study', 'Can Resubmit Study'), ('can_edit__study_permissions', 'Can Edit Study Permissions'), ('can_view_study_permissions', 'Can View Study Permissions'), ('can_view_study_responses', 'Can View Study Responses'), ('can_view_study_video_responses', 'Can View Study Video Responses'), ('can_view_study_demographics', 'Can View Study Demographics'))},
        ),
    ]