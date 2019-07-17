from django.urls import include, path, re_path, register_converter
from django.contrib import admin
from django.views.generic import TemplateView

from coffeehouse.utils import converters

register_converter(converters.RomanNumeralConverter, 'roman')
register_converter(converters.FloatConverter, 'float')

# Overrides the default 400 handler django.views.defaults.bad_request
handler400 = 'coffeehouse.utils.views.bad_request'
# Overrides the default 403 handler django.views.defaults.permission_denied
handler403 = 'coffeehouse.utils.views.permission_denied'
# Overrides the default 404 handler django.views.defaults.page_not_found
handler404 = 'coffeehouse.utils.views.page_not_found'
# Overrides the default 500 handler django.views.defaults.server_error
handler500 = 'coffeehouse.utils.views.server_error'
    
urlpatterns = [
    path('',TemplateView.as_view(template_name='homepage.html'),name="homepage"),
    path('<roman:roman_number>/',TemplateView.as_view(template_name='homepage.html')),
    path('<float:float_number>/',TemplateView.as_view(template_name='homepage.html')),            
    path('about/',include('coffeehouse.about.urls',namespace="about")),
    path('drinks/<str:drink_type>/',TemplateView.as_view(template_name='drinks/index.html'),{'onsale':True},name="drink_type"),
    path('stores/',include('coffeehouse.stores.urls',namespace="stores")),
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    path('coffeebanners/',include('coffeehouse.banners.urls',namespace="coffee-banners")),
    path('teabanners/',include('coffeehouse.banners.urls',namespace="tea-banners")),
    path('foodbanners/',include('coffeehouse.banners.urls',namespace="food-banners")),
]
