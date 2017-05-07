from django.conf.urls import include, url
from django.views.generic import TemplateView
from django.contrib import admin


from coffeehouse.drinks.urls import urlpatterns as drinks_url_patterns

urlpatterns = [
    url(r'^$',TemplateView.as_view(template_name='homepage.html'),name="homepage"),
    url(r'^about/', include('coffeehouse.about.urls',namespace="about")),
    url(r'^drinks/', include(drinks_url_patterns,namespace="drinks")),
    url(r'^stores/',include('coffeehouse.stores.urls',namespace="stores")),
    url(r'^online/',include('coffeehouse.online.urls',namespace="online")),
    url(r'^social/',include('coffeehouse.social.urls',namespace="social")),    
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', admin.site.urls),
]
