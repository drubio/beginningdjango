# Create your views here.
from django.shortcuts import render
from django.core.exceptions import PermissionDenied,SuspiciousOperation
from django.http import Http404

def index(request,store_id=1,location=None):
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
    if float(longitude) == 90 or float(longitude) == 90:
        return HttpResponsePermanentRedirect("http://maps.google.com/")
    # Create fixed data structures to pass to template
    # data could equally come from database queries
    store = {'name':'Downtown','address':'Main #385','city':'San Diego','state':'CA'}
    store_amenities = ['WiFi','A/C']
    store_menu = ((0,''),(1,'Drinks'),(2,'Food'))
    vals_for_template = {'store':store,'store_amenities':store_amenities,'store_menu':store_menu}
    return render(request,'stores/index.html', vals_for_template)
