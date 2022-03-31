from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import include, path
import debug_toolbar

from coffeehouse.drinks.urls import urlpatterns as drinks_url_patterns

urlpatterns = [
    path('',TemplateView.as_view(template_name='homepage.html'),name="homepage"),
    path('about/',include('coffeehouse.about.urls')),
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    path('drinks/', include((drinks_url_patterns,'coffeehouse.drinks'))),
    path('online/',TemplateView.as_view(template_name='online/index.html'),name='online'),
    path('stores/',include('coffeehouse.stores.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
]
