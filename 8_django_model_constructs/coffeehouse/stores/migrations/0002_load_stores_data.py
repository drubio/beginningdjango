# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations

def load_store_amenities_from_sql():
    from django.conf import settings
    import os
    sql_statements = open(os.path.join(settings.PROJECT_DIR,'stores/sql/store_amenities.sql'), 'r').read()
    return sql_statements

def delete_store_amenities_from_sql():
    return "DELETE from stores_store_amenities"; #sql_statements

def delete_stores(apps, schema_editor):
    Amenity = apps.get_model("stores", "Store")
    Amenity.objects.all().delete()
    
def load_amenities(apps, schema_editor):
    Amenity = apps.get_model("stores", "Amenity")
    amenity_wifi = Amenity(name='WiFi',description='Just consult your purchase ticket to access our Wifi password and surf the net while you enjoy your coffee')
    amenity_wifi.save()
    amenity_ac = Amenity(name='A/C',description='Enjoy our store environment with state of the art temperature and humidity controls')
    amenity_ac.save()
    amenity_parking = Amenity(name='Parking',description='Free parking with purchases over $10')
    amenity_parking.save()
    amenity_laptop = Amenity(name='Laptop locks',description='Ask our baristas for a laptop lock on your first order, so you can freely move around our store')
    amenity_laptop.save()    
    amenity_newspapers = Amenity(name='Newspapers',description='Enjoy reading free daily newspapers and take a break from digitial media')
    amenity_newspapers.save()    


def delete_amenities(apps, schema_editor):
    Amenity = apps.get_model("stores", "Amenity")
    Amenity.objects.all().delete()

    
def load_stores_from_fixture(apps, schema_editor):
    from django.core.management import call_command
    call_command("loaddata", "stores")

class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_amenities,delete_amenities),
        migrations.RunPython(load_stores_from_fixture,delete_stores),
        migrations.RunSQL(load_store_amenities_from_sql(),delete_store_amenities_from_sql()),
    ]
