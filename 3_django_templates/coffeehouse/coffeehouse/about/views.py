# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
    return render_to_response('about/index.html',context_instance=RequestContext(request))

def contact(request):
    return render_to_response('about/contact.html',context_instance=RequestContext(request))
