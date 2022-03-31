from django.urls import include, path
from . import views 
from . import apps

app_name = apps.StoresConfig.name

urlpatterns = [
    path('',views.index,name="index"),
    path('<int:store_id>/',views.detail,name="detail"),
    path('<int:store_id>/about/',include(('coffeehouse.about.urls'), namespace="nested-stores-about")),
]
