from django.contrib import admin

from django.contrib import admin
from .models import CoffeehouseUser

class CoffeehouseUserAdmin(admin.ModelAdmin):
    pass

admin.site.register(CoffeehouseUser, CoffeehouseUserAdmin)
