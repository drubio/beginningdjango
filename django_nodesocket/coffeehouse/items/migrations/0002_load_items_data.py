# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


def load_items_from_fixture(apps, schema_editor):
    from django.core.management import call_command
    call_command("loaddata", "items")

class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_items_from_fixture)
    ]
