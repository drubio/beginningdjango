from django.contrib import admin
from coffeehouse.stores.models import Amenity, Store, Special

# Register your models here.
class AmenityAdmin(admin.ModelAdmin):
    pass

admin.site.register(Amenity, AmenityAdmin)

class StoreAdmin(admin.ModelAdmin):
    pass

admin.site.register(Store, StoreAdmin)

class SpecialAdmin(admin.ModelAdmin):
    pass

admin.site.register(Special, SpecialAdmin)
