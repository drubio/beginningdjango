from django.conf.urls import include, url
from coffeehouse.items import views as items_views

urlpatterns = [
    url(r'^$',items_views.index,name="index"),
    url(r'^(?P<item_id>\d+)/$',items_views.detail,name="detail"),
]
