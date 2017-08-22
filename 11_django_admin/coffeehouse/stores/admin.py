# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from coffeehouse.stores.models import Store,Amenity


class StoreAdmin(admin.ModelAdmin):
    search_fields = ['city','state']
    list_display = ['name','full_address','list_of_amenities']
    list_filter = [['amenities',admin.RelatedOnlyFieldListFilter]]
    def list_of_amenities(self, obj):
        return ("%s" % ','.join([amenity.name for amenity in obj.amenities.all()]))
    list_of_amenities.short_description = 'Store amenities'         
    filter_horizontal = ['amenities']
    prepopulated_fields = {'address': ['city','state']}
    def changelist_view(self, request, extra_context=None):
        # Add extra context data to pass to change list template
        extra_context = extra_context or {}
        extra_context['my_store_data'] = {'onsale':['Item 1','Item 2']}
        # Execute default logic from parent class changelist_view()
        return super(StoreAdmin, self).changelist_view(
            request, extra_context=extra_context
        )
    def delete_view(self, request, object_id, extra_context=None):
        # Add custom audit logic here
        #
        # Execute default logic from parent class delete_view()
        return super(StoreAdmin, self).delete_view(
            request, object_id, extra_context=extra_context
        )
    
admin.site.register(Store, StoreAdmin)

from coffeehouse.admin import provideradmin
provideradmin.register(Store, StoreAdmin)

class StoreInline(admin.TabularInline):
    model = Store.amenities.through
    
class AmenityAdmin(admin.ModelAdmin):
    inlines = [
        StoreInline,
    ]

admin.site.register(Amenity, AmenityAdmin)
