from django.conf.urls import url

urlpatterns = [
    url(r'^$','coffeehouse.banners.views.index',name="index"),
]
