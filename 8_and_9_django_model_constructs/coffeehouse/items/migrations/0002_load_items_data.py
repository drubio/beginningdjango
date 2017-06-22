# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


def load_items_from_fixture(apps, schema_editor):
    from django.core.management import call_command
    call_command("loaddata", "items")

def delete_all_items(apps, schema_editor):
    Items = apps.get_model("items", "Item")
    Items.objects.all().delete()

    
class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_items_from_fixture,delete_all_items)
    ]
