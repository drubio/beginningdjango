from django.urls import path
from . import views

app_name = 'about'

urlpatterns = [
    path('',views.index,name="index"),
    path('<int:store_id>/',views.index,name="index_withid"),
    path('contact/',views.ContactPage.as_view(),name="contact"),
    path('contact/<int:store_id>/',views.ContactPage.as_view(),name="contact_withid"),
]
