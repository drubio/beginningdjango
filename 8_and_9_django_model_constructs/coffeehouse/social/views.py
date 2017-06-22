from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import SharingForm
from django.conf import settings

# Create your views here.
def index(request):
    if request.method == 'POST':
        # POST, generate form with data from the request
        form = SharingForm(request.POST,request.FILES)
        # check if it's valid:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/about/contact/thankyou')
    else:
        # GET, generate blank form
        form = SharingForm()
    return render(request,'social/index.html',{'form':form})
