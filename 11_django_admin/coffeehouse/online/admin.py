from django.contrib import admin

# Register your models here.
from coffeehouse.online.models import Order

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'

admin.site.register(Order, OrderAdmin)
