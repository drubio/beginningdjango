from django.conf.urls import patterns, url

urlpatterns = patterns('coffeehouse.banners.views',
    url(r'^$','index',name="index"),
)
