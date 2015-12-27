from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from coffeehouse.about import views as about_views

urlpatterns = [
    url(r'^$',TemplateView.as_view(template_name='homepage.html')),
    url(r'^about/',about_views.contact),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', admin.site.urls),
]
