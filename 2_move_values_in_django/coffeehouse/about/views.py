# Create your views here.
from django.shortcuts import render

def index(request):
    return render(request,'about/index.html')

def contact(request):
    return render(request,'about/contact.html')
