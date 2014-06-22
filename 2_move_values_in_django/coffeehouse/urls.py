from django.conf.urls import patterns, include, url
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

urlpatterns = patterns('',
    url(r'^$',TemplateView.as_view(template_name='homepage.html')),
    url(r'^about/contact','coffeehouse.about.views.contact'),
    url(r'^about/','coffeehouse.about.views.index'),
    url(r'^drinks/(?P<drink_type>\D+)/',TemplateView.as_view(template_name='drinks/index.html'),{'onsale':True}),
    url(r'^stores/(?P<store_id>\d+)/','coffeehouse.stores.views.index'),
    url(r'^stores/','coffeehouse.stores.views.index',{'location':'headquarters'}),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
