from django.conf.urls import include, url
from coffeehouse.drinks import views as drinks_views

urlpatterns = [
    url(r'^$',drinks_views.index,name="index"),
    url(r'^(?P<drink_type>\D+)/$',drinks_views.detail,name="detail"),
]
