from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index,name="index"),
    url(r'^(?P<store_id>\d+)/$',views.index,name="index_withid"),
    url(r'^contact/$',views.contact,name="contact"),
    url(r'^contact/(?P<store_id>\d+)/$',views.contact,name="contact_withid"),
]
