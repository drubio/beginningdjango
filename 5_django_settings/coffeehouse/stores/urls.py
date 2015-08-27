from django.conf.urls import include, url

urlpatterns = [
    url(r'^$','coffeehouse.stores.views.index',name="index"),
    url(r'^(?P<store_id>\d+)/$','coffeehouse.stores.views.detail',name="detail"),
    url(r'^(?P<store_id>\d+)/about/',include('coffeehouse.about.urls',namespace="about")),
]
