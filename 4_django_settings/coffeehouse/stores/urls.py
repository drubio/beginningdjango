from django.conf.urls import patterns, include, url

urlpatterns = patterns('coffeehouse.stores.views',
    url(r'^$','index',name="index"),
    url(r'^(?P<store_id>\d+)/$','detail',name="detail"),
    url(r'^(?P<store_id>\d+)/about/',include('coffeehouse.about.urls',namespace="about")),
)
