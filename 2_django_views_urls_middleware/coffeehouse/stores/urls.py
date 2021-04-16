from django.urls import include, path

from . import views 

app_name = 'about'

urlpatterns = [
    path('',views.index,name="index"),
    path('<int:store_id>/',views.detail,name="detail"),
    path('<int:store_id>/about/',include('coffeehouse.about.urls',namespace="stores_about")),
]
