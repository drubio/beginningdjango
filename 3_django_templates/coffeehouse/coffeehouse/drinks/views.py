# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
    drink_list = ['mocha','espresso','latte']
    return render_to_response('drinks/index.html',{'drinks':drink_list}, context_instance=RequestContext(request))

def detail(request,drink_type):
    if drink_type == "mocha":
        description = "Our superior dark coffee made from beans from Arabia"
    elif drink_type == "espresso":
        description = "Our strong coffee brewed by forcing steam under pressure through darkly roasted, powdered coffee beans"
    else: 
        description = "Our coffee made with hot milk"
    return render_to_response('drinks/detail.html',{'drink':drink_type,'drink_description':description}, context_instance=RequestContext(request))    
