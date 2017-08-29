from django.conf.urls import include, url
from coffeehouse.items import views as items_views

urlpatterns = [
    url(r'^$',items_views.ItemList.as_view(),name="index"),
    url(r'^(?P<item_id>\d+)/$',items_views.ItemDetail.as_view(),name="detail"),
    url(r'^new/$', items_views.ItemCreation.as_view(), name='new'),
    url(r'^edit/(?P<item_id>\d+)/$', items_views.ItemUpdate.as_view(), name='edit'),
    url(r'^delete/(?P<item_id>\d+)/$', items_views.ItemDelete.as_view(), name='delete'),    
]
