# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
from django.http import Http404, HttpResponse, JsonResponse
from coffeehouse.stores.models import Store
from coffeehouse.stores.forms import ContactCommentOnlyForm

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views import View


class StoreList(ListView):
    model = Store

class StoreDetail(DetailView):
    model = Store
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(StoreDetail, self).get_context_data(**kwargs)
        # Add ContactCommentOnlyForm to context
        form = ContactCommentOnlyForm()        
        context['form'] = form
        return context

class StoreFeedbackView(View):
    # Get handler method
    def get(self, request):
        return HttpResponse("Hello from feedback!")

    # Post handler method
    def post(self, request):
        form = ContactCommentOnlyForm(request.POST)
        if form.is_valid():
            return JsonResponse({'success':True})
        else:
            return JsonResponse({'error':form.errors})


from rest_framework import viewsets

from coffeehouse.stores.serializers import StoreSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

class StoreViewSet(viewsets.ModelViewSet):
    """
    Return a list of all the Store records.
    """    
    permission_classes = (IsAuthenticated,)
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
