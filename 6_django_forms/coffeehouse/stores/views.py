# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
from django.shortcuts import render
from django.core.exceptions import PermissionDenied,SuspiciousOperation
from django.http import Http404, HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect, JsonResponse
from .forms import ContactCommentOnlyForm

STORE_LIST =  [{'id':0,'name':'Corporate','address':'624 Broadway','city':'San Diego','state':'CA','email':'corporate@coffeehouse.com'},{'id':1,'name':'Downtown','address':'Horton Plaza','city':'San Diego','state':'CA','email':'downtown@coffeehouse.com'},{'id':2,'name':'Uptown','address':'1240 University Ave','city':'San Diego','state':'CA','email':'uptown@coffeehouse.com'},{'id':3,'name':'Midtown','address':'784 W Washington St','city':'San Diego','state':'CA','email':'midtown@coffeehouse.com'}]

def index(request,location=None):
    store_list = STORE_LIST[1:]
    return render(request,'stores/index.html',  {'stores':store_list})    

def detail(request,store_id=1,location=None):
    # Access store_id parameter with 'store_id' variable 
    # Access location parameter with 'location' variable
    # Extract 'hours', 'lat' or 'lon' values appended to url as
    # e.g. ?hours=sunday&latitude=32.71&longitude=-117.16
    # 'hours' has value 'sunday' or '' if hours not in url
    # 'latitude' has value 32.71 or 0 if latitude not in url
    # 'longitude' has value -117.16 or 0 if longitude not in url
    hours = request.GET.get('hours', '')
    latitude = request.GET.get('latitude', 0)
    longitude = request.GET.get('longitude', 0)    
    # Validation for hours variables
    if hours not in ['','sunday','monday','tuesday','wednesday','thursday','friday','saturday']:
        raise Http404
    # Validation for latitude & longitude 
    try:
        # latitude and longitude should be cast'able to float if numbers
        float(latitude)
        float(longitude)
    except ValueError:
        raise SuspiciousOperation
    # Validation if latitude in range
    if float(latitude) > 90 or float(latitude) < -90:
        raise Exception("Invalid latitude, min -90 and max 90")
    # Validation if longitude in range
    if float(longitude) > 180 or float(longitude) < -180:
        raise Exception("Invalid longitude, min -180 and max 180")
    # If latitude==90 and longitude==90, redirect to maps.google.com
    if float(latitude) == 90 or float(longitude) == 90:
        return HttpResponsePermanentRedirect("http://maps.google.com/")
    # Create fixed data structures to pass to template
    # data could equally come from database queries
    if store_id == "1":
        store = STORE_LIST[1]
    elif store_id == "2":
        store = STORE_LIST[2]
    elif store_id == "3":
        store = STORE_LIST[3]
    else:
        raise Http404
    store_amenities = ['WiFi','A/C']
    store_menu = ((0,''),(1,'Drinks'),(2,'Food'))
    form = ContactCommentOnlyForm()
    vals_for_template = {'store':store,'store_amenities':store_amenities,'store_menu':store_menu,'form':form}
    return render(request,'stores/detail.html', vals_for_template)

def feedback(request,store_id=1):
    if request.POST:
        form = ContactCommentOnlyForm(request.POST)
        if form.is_valid():
            return JsonResponse({'success':True})
        else:
            return JsonResponse({'error':form.errors})
    return HttpResponse("Hello from feedback!")
