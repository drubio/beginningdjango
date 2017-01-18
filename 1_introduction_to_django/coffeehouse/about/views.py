# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def contact(request):
    return render(request,'about/contact.html')
