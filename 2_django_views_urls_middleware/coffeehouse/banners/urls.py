from django.urls import path
from . import views 
from . import apps

app_name = apps.BannersConfig.name

urlpatterns = [
    path(r'',views.index,name="index"),
]
