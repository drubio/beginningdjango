from django.urls import path
from . import views 

app_name = 'banners_adverts'
urlpatterns = [
    path(r'',views.index,name="index"),
]
