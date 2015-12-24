from django.conf.urls import include, url

urlpatterns = [
    url(r'^$','coffeehouse.drinks.views.index',name="index"),
    url(r'^(?P<drink_type>\D+)/$','coffeehouse.drinks.views.detail',name="detail"),
]
