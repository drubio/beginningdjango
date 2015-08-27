# Create your views here.
from django.shortcuts import render
from coffeehouse.stores.views import STORE_LIST
from django.http import Http404

# Python logging library
import logging

# Standard instance of a logger with __name__
stdlogger = logging.getLogger(__name__)
stdlogger.setLevel(logging.DEBUG)

def index(request,store_id=None):
    stdlogger.debug("Call to index method")
    # Create fixed data structures to pass to template
    # data could equally come from database queries
    stdlogger.debug("Entering store_id conditional block with store_id=%s" % store_id)
    if store_id == None:
        store = STORE_LIST[0]
    elif store_id == "1":
        store = STORE_LIST[1]
    elif store_id == "2":
        store = STORE_LIST[2]
    elif store_id == "3":
        store = STORE_LIST[3]
    else:
        raise Http404
    return render(request,'about/index.html',{'store':store})

def contact(request,store_id=None):
    stdlogger.info("Call to contact method")
    # Create fixed data structures to pass to template
    # data could equally come from database queries
    stdlogger.debug("Entering store_id conditional block with store_id=%s" % store_id)
    if store_id == None:
        store = STORE_LIST[0]
    elif store_id == "1":
        store = STORE_LIST[1]
    elif store_id == "2":
        store = STORE_LIST[2]
    elif store_id == "3":
        store = STORE_LIST[3]
    else:
        raise Http404
    return render(request,'about/contact.html',{'store':store})
