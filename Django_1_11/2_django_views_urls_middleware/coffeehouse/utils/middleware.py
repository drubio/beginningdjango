# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging

stdlogger = logging.getLogger(__name__)

class CoffeehouseMiddleware(object):

    def __init__(self, get_response):
        stdlogger.info("Start CoffehouseMiddleware __init__")
        self.get_response = get_response
        stdlogger.info("End CoffehouseMiddleware __init__")

    def __call__(self, request):
        stdlogger.info("Start CoffehouseMiddleware __call__")

        stdlogger.info("CoffehouseMiddleware __call__ before get_response")
        response = self.get_response(request)
        stdlogger.info("CoffehouseMiddleware __call__ after get_response")
        
        stdlogger.info("End CoffehouseMiddleware __call__")
        return response
    
    def process_view(self, request, view_func, view_args, view_kwargs):
        """ Called on each request, just before Django calls the view.
        Keyword arguments:
        request -- the HttpRequest object. 
        view_func -- the Python function that Django is about to use. It's the actual function object, not the name of the function as a string.
        view_args -- a list of positional arguments that will be passed to the view. Does not include the first view argument (request).
        view_kwargs -- a dictionary of keyword arguments that will be passed to the view. Does not include the first view argument (request).
        Response value:   
        None -- An empty value; If it returns None, Django will continue processing this request, executing any other process_view() middleware and, then, the appropriate view. 
        HttpResponse -- An HttpResponse object; If it returns an HttpResponse object, Django won't bother calling any other view or exception middleware, or the appropriate view; it'll apply response middleware to that HttpResponse, and return the result.
        NOTE: Request-phase method applied in order, from the top to bottom. This means classes defined at the start of MIDDLEWARE will be run first.
        """
        stdlogger.info("Start CoffehouseMiddleware process_view")
        stdlogger.info("End CoffehouseMiddleware process_view")
        return None
    
    
    def process_exception(self,request, exception):
        """ Called when a view raises an exception.
        Keyword arguments:
        request -- the HttpRequest object. 
        exception -- an Exception object raised by the view function.
        Response value: 
        None -- An empty value; the default exception handling kicks in.
	HttpResponse -- An HttpResponse object; If it returns an HttpResponse object, the template response and response middleware will be applied, and the resulting response returned to the browser. If an exception middleware returns a response, the middleware classes above that middleware will not be called at all.
        NOTE: Response-phase method applied in reverse order, from the bottom up. This means classes defined at the end of MIDDLEWARE will be run first.
        """
        stdlogger.info("Start CoffehouseMiddleware process_exception")
        stdlogger.info("End CoffehouseMiddleware process_exception")
        return None
    
    def process_template_response(self,request, response):
        """  Called just after the view has finished executing.
        Keyword arguments:
        request -- the HttpRequest object. 
        response -- the TemplateResponse object (or equivalent) returned by a Django view or by a middleware.
        Response value: 
        TemplateResponse or equivalent response object that implements a render method. It could alter the given response by changing response.template_name and response.context_data, or it could create and return a brand-new TemplateResponse or equivalent.
        NOTE: You don't need to explicitly render responses, responses are automatically rendered once all template response middleware has been called.
        NOTE2: Response-phase method applied in reverse order, from the bottom up. This means classes defined at the end of MIDDLEWARE will be run first.
        """
        stdlogger.info("Start CoffehouseMiddleware process_template_response")
        stdlogger.info("End CoffehouseMiddleware process_template_response")
        return response
