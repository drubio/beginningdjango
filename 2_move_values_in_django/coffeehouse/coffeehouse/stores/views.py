# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request,store_id=1,location=''):
    # Access store_id parameter with 'store_id' variable 
    # Access location parameter with 'location' variable
    # Extract 'hours' or 'map' value appended to url as
    # ?hours=sunday&map=flash
    hours = request.GET.get('hours', '')
    map = request.GET.get('map', '')
    # 'hours' has value 'sunday' or '' if hours not in url
    # 'hours' has value 'flash' or '' if map not in url
    # Create fixed data structures to pass to template
    # data could equally come from database queries
    STORE_NAME = 'Downtown'
    store_address = {'street':'Main #385','city':'San Diego','state':'CA'}
    store_amenities = ['WiFi','A/C']
    store_menu = ((0,''),(1,'Drinks'),(2,'Food'))
    vals_for_template = {'store_name':STORE_NAME,'store_address':store_address,'store_amenities':store_amenities,'store_menu':store_menu}
    return render_to_response('stores/index.html', vals_for_template, context_instance=RequestContext(request))
