# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import TemplateView
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.AboutDetail.as_view(),name="index"),
    url(r'^(?P<store_id>\d+)/$',views.AboutDetail.as_view(),name="index_withid"),
    url(r'^contact/$',views.Contact.as_view(),name="contact"),
    url(r'^contact/thankyou$',TemplateView.as_view(template_name='about/thankyou.html'),name="contact_thankyou"),
]
