from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from coffeehouse.about import views as about_views

urlpatterns = [
    path('',TemplateView.as_view(template_name='homepage.html')),
    path('about/',about_views.contact),
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
]
