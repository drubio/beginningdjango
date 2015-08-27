from django.conf.urls import include, url

urlpatterns = [
    url(r'^$','coffeehouse.about.views.index',name="index"),
    url(r'^(?P<store_id>\d+)/$','coffeehouse.about.views.index',name="index_withid"),
    url(r'^contact/$','coffeehouse.about.views.contact',name="contact"),
    url(r'^contact/(?P<store_id>\d+)/$','coffeehouse.about.views.contact',name="contact_withid"),
]
