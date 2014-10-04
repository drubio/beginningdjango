from django.shortcuts import render
from django.core.urlresolvers import resolve

def index(request):    
    return render(request,'banners/index.html',current_app=resolve(request.path).namespace)
