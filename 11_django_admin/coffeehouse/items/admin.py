from django.contrib import admin
from coffeehouse.items.models import Menu, Item, Drink

class ItemInline(admin.StackedInline):
    model = Item
    
class MenuAdmin(admin.ModelAdmin):
    list_display = ['name','creator']
    inlines = [
        ItemInline,
    ]
    
admin.site.register(Menu, MenuAdmin)

from coffeehouse.admin import employeeadmin
employeeadmin.register(Menu, MenuAdmin)

class ItemAdmin(admin.ModelAdmin):
    list_per_page = 5
    list_display = ['menu','name','menu_creator']
    list_filter = ['menu','name','menu__creator']    
    def menu_creator(self, obj):
        return obj.menu.creator
    menu_creator.admin_order_field = 'menu__creator'
    radio_fields = {"menu": admin.HORIZONTAL}    
    save_as = True
    save_as_continue = False
    class Media:
        css = {
            "screen": ("css/items/items.css",)
        }
        js = ("js/items/items.js",)
    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser and request.user.has_perm('items.read_item'):
            return [f.name for f in self.model._meta.fields]        
        return super(ItemAdmin, self).get_readonly_fields(
            request, obj=obj
        )
    
admin.site.register(Item, ItemAdmin)

class DrinkAdmin(admin.ModelAdmin):
    pass

admin.site.register(Drink, DrinkAdmin)
