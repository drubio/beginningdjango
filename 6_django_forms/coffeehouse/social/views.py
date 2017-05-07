from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import SharingForm
from django.conf import settings


def save_uploaded_file_to_media_root(f):
    #print('%s,%s,%s,%s' % (f.name,f.size,f.content_type,dir(userfile)))
    with open('%s%s' % (settings.MEDIA_ROOT,f.name), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
            
# Create your views here.
def index(request):
    if request.method == 'POST':
        # POST, generate form with data from the request
        form = SharingForm(request.POST,request.FILES)
        # check if it's valid:
        if form.is_valid():
            for field in request.FILES.keys():
                for formfile in request.FILES.getlist(field):
                    save_uploaded_file_to_media_root(formfile)                    
            return HttpResponseRedirect('/about/contact/thankyou')
    else:
        # GET, generate blank form
        form = SharingForm()
    return render(request,'social/index.html',{'form':form})
