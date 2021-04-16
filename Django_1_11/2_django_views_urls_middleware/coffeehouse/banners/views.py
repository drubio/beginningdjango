# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.urlresolvers import resolve

def index(request):    
    return render(request,'banners/index.html')
