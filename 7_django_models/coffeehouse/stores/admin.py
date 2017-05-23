# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from coffeehouse.stores.models import Amenity, Store

class AmenityAdmin(admin.ModelAdmin):
    pass

admin.site.register(Amenity, AmenityAdmin)

class StoreAdmin(admin.ModelAdmin):
    pass

admin.site.register(Store, StoreAdmin)

