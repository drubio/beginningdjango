# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import include, url

from . import views 

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'stores', views.StoreViewSet)


urlpatterns = [
    url(r'^$',views.StoreList.as_view(),name="index"),
    url(r'^rest/', include(router.urls,namespace="rest")),
    url(r'^feedback/$',views.StoreFeedbackView.as_view(),name="feedback"),    
    url(r'^(?P<pk>\d+)/$',views.StoreDetail.as_view(),name="detail"),
    url(r'^(?P<store_id>\d+)/about/',include('coffeehouse.about.urls',namespace="stores_about")),
]
