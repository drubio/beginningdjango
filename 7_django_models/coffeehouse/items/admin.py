from django.contrib import admin
from coffeehouse.items.models import Menu, Item, Drink

# Register your models here.
class MenuAdmin(admin.ModelAdmin):
    pass

admin.site.register(Menu, MenuAdmin)

class ItemAdmin(admin.ModelAdmin):
    pass

admin.site.register(Item, ItemAdmin)

class DrinkAdmin(admin.ModelAdmin):
    pass

admin.site.register(Drink, DrinkAdmin)
