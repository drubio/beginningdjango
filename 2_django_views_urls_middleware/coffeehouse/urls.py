from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

# Overrides the default 400 handler django.views.defaults.bad_request
handler400 = 'coffeehouse.utils.views.bad_request'
# Overrides the default 403 handler django.views.defaults.permission_denied
handler403 = 'coffeehouse.utils.views.permission_denied'
# Overrides the default 404 handler django.views.defaults.page_not_found
handler404 = 'coffeehouse.utils.views.page_not_found'
# Overrides the default 500 handler django.views.defaults.server_error
handler500 = 'coffeehouse.utils.views.server_error'
    
urlpatterns = [
    url(r'^$',TemplateView.as_view(template_name='homepage.html'),name="homepage"),
    url(r'^about/',include('coffeehouse.about.urls',namespace="about")),
    url(r'^drinks/(?P<drink_type>\D+)/',TemplateView.as_view(template_name='drinks/index.html'),{'onsale':True},name="drink_type"),
    url(r'^stores/',include('coffeehouse.stores.urls',namespace="stores")),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^coffeebanners/',include('coffeehouse.banners.urls',namespace="coffee-banners",app_name="banners_adverts")),
    url(r'^teabanners/',include('coffeehouse.banners.urls',namespace="tea-banners",app_name="banners_adverts")),
    url(r'^foodbanners/',include('coffeehouse.banners.urls',namespace="food-banners",app_name="banners_adverts")),
]
