from django.urls import include, path
from . import views 
from . import apps

app_name = apps.DrinksConfig.name

urlpatterns = [
    path('',views.index,name="index"),
    path('<str:drink_type>/',views.detail,name="detail"),
]
