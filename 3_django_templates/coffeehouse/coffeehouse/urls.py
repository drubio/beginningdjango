from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$','django.views.generic.simple.direct_to_template', {'template': 'homepage.html','homepage':True,'thejs':'"mocha\r\n \'price:2.25"'}),
    url(r'^about/contact','coffeehouse.about.views.contact'),
    url(r'^about/','coffeehouse.about.views.index'),
    url(r'^drinks/(?P<drink_type>\D+)','coffeehouse.drinks.views.detail'),
    url(r'^drinks/','coffeehouse.drinks.views.index'),
    url(r'^stores/(?P<store_id>\d+)','coffeehouse.stores.views.detail'),
    url(r'^stores/','coffeehouse.stores.views.index'),
    url(r'^online/','django.views.generic.simple.direct_to_template', {'template': 'online/index.html'}),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
