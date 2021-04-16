# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$',views.index,name="index"),
    url(r'^(?P<store_id>\d+)/$',views.index,name="index_withid"),
    url(r'^contact/$',views.ContactPage.as_view(),name="contact"),
    url(r'^contact/(?P<store_id>\d+)/$',views.ContactPage.as_view(),name="contact_withid"),
]
