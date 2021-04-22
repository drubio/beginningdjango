from django.urls import path
from . import views
from . import apps

app_name = apps.AboutConfig.name

urlpatterns = [
    path('',views.index,name="index"),
    path('<int:store_id>/',views.index,name="index_withid"),
    path('contact/',views.contact,name="contact"),
    path('contact/<int:store_id>/',views.contact,name="contact_withid"),
]
