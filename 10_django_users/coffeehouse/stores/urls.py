# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import include, url

from . import views 

urlpatterns = [
    url(r'^$',views.StoreList.as_view(),name="index"),
    url(r'^feedback/$',views.StoreFeedbackView.as_view(),name="feedback"),    
    url(r'^(?P<pk>\d+)/$',views.StoreDetail.as_view(),name="detail"),
    url(r'^(?P<store_id>\d+)/about/',include('coffeehouse.about.urls',namespace="stores_about")),
]
