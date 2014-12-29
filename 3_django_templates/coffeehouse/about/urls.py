from django.conf.urls import patterns, include, url

urlpatterns = patterns('coffeehouse.about.views',
    url(r'^$','index',name="index"),
    url(r'^(?P<store_id>\d+)/$','index',name="index_withid"),
    url(r'^contact/$','contact',name="contact"),
    url(r'^contact/(?P<store_id>\d+)/$','contact',name="contact_withid"),
)
