# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-01 09:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_squashed_0003_auto_20160207_1550'),
        ('meetup', '0013_auto_20180224_2101'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='meetuplocation',
            options={'permissions': (('add_meetup_location_member', 'Add meetup location member'), ('delete_meetup_location_member', 'Delete meetup location member'), ('add_meetup_location_moderator', 'Add meetup location moderator'), ('delete_meetup_location_moderator', 'Delete meetup location moderator'), ('approve_meetup_location_joinrequest', 'Approve meetup location join request'), ('reject_meetup_location_joinrequest', 'Reject meetup location join request'), ('approve_meetup_comment', 'Approve comment for a meetup'), ('reject_meetup_comment', 'Reject comment for a meetup'), ('add_meetup_rsvp', 'RSVP for a meetup'), ('approve_support_request', 'Approve support request'), ('reject_support_request', 'Reject support request'), ('add_support_request_comment', 'Add comment for a support request'), ('edit_support_request_comment', 'Edit comment for a support request'), ('delete_support_request_comment', 'Delete comment for a support request'), ('approve_support_request_comment', 'Approve comment for a support request'), ('reject_support_request_comment', 'Reject comment for a support request'))},
        ),
        migrations.RemoveField(
            model_name='meetuplocation',
            name='organizers',
        ),
        migrations.AddField(
            model_name='meetuplocation',
            name='leader',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='community_leader', to='users.SystersUser', verbose_name='Community leader'),
        ),
        migrations.AddField(
            model_name='meetuplocation',
            name='moderators',
            field=models.ManyToManyField(related_name='community_moderators', to='users.SystersUser', verbose_name='Community Moderators'),
        ),
        migrations.AlterField(
            model_name='meetuplocation',
            name='members',
            field=models.ManyToManyField(blank=True, related_name='community_members', to='users.SystersUser', verbose_name='Community Members'),
        ),
    ]
