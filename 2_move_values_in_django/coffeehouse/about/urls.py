from django.conf.urls import patterns, include, url

urlpatterns = patterns('coffeehouse.about.views',
    url(r'^$','index',name="index"),
    url(r'^contact/$','contact',name="contact"),
)
