from django.conf.urls import include, url
from coffeehouse.stores import views as stores_views

urlpatterns = [
    url(r'^$',stores_views.index,name="index"),
    url(r'^(?P<store_id>\d+)/$',stores_views.detail,name="detail"),
    url(r'^(?P<store_id>\d+)/about/',include('coffeehouse.about.urls',namespace="about")),
]
