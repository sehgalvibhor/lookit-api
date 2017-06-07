# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-15 20:28
from __future__ import unicode_literals

from django.contrib.flatpages.models import FlatPage
from django.contrib.sites.models import Site
from django.db import migrations

flatpages = [
    dict(url='/', title='Home', content='Home'),
    dict(url='/faq', title='FAQ', content='FAQ'),
    dict(url='/scientists', title='The Scientists', content='The Scientists'),
    dict(url='/resources', title='Resources', content='Resources'),
    dict(url='/contact', title='Contact Us', content='Contact Us'),
]


def make_pages(*args, **kwargs):
    site, created = Site.objects.get_or_create(domain='example.com', defaults={'name': 'Example'})
    for page in flatpages:
        flatpage_obj, created = FlatPage.objects.get_or_create(**page)
        flatpage_obj.sites.add(site)


def unmake_pages(*args, **kwargs):
    FlatPage.objects.filter(url__in=[page['url'] for page in flatpages]).delete()


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.RunPython(make_pages, reverse_code=unmake_pages)
    ]
