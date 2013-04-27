from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$',TemplateView.as_view(template_name='homepage.html'),{'homepage':True,'thejs':'"mocha\r\n \'price:2.25"'}),
    url(r'^about/contact','coffeehouse.about.views.contact'),
    url(r'^about/','coffeehouse.about.views.index'),
    url(r'^drinks/(?P<drink_type>\D+)','coffeehouse.drinks.views.detail'),
    url(r'^drinks/','coffeehouse.drinks.views.index'),
    url(r'^stores/(?P<store_id>\d+)','coffeehouse.stores.views.detail'),
    url(r'^stores/','coffeehouse.stores.views.index'),
    url(r'^online/',TemplateView.as_view(template_name='online/index.html')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
