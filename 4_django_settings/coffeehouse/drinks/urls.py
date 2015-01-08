from django.conf.urls import patterns, include, url

urlpatterns = patterns('coffeehouse.drinks.views',
    url(r'^$','index',name="index"),
    url(r'^(?P<drink_type>\D+)/$','detail',name="detail"),
)
