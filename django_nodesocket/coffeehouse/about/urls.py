from django.conf.urls import include, url
from coffeehouse.about import views as about_views

urlpatterns = [
    url(r'^$',about_views.index,name="index"),
    url(r'^(?P<store_id>\d+)/$',about_views.index,name="index_withid"),
    url(r'^contact/$',about_views.contact,name="contact"),
    url(r'^contact/(?P<store_id>\d+)/$',about_views.contact,name="contact_withid"),
]
