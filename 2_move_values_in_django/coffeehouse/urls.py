from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$',TemplateView.as_view(template_name='homepage.html')),
    url(r'^about/','coffeehouse.about.views.contact'),
    url(r'^drinks/(?P<drink_type>\D+)',TemplateView.as_view(template_name='drinks/index.html'),{'onsale':True}),
    url(r'^stores/(?P<store_id>\d+)','coffeehouse.stores.views.index'),
    url(r'^stores/','coffeehouse.stores.views.index',{'location':'headquarters'}),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

)
