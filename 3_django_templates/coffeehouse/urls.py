from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from coffeehouse.drinks.urls import urlpatterns as drinks_url_patterns

urlpatterns = patterns('',
    url(r'^$',TemplateView.as_view(template_name='homepage.html'),{'homepage':True,'thejs':'"mocha\r\n \'price:2.25"'}),
    url(r'^about/', include('coffeehouse.about.urls',namespace="about")),
    url(r'^drinks/', include(drinks_url_patterns,namespace="drinks")),
    url(r'^stores/',include('coffeehouse.stores.urls',namespace="stores")),
    url(r'^online/',TemplateView.as_view(template_name='online/index.html')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
