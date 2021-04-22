# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
from django.shortcuts import render

def index(request):
    drink_list = ['mocha','espresso','latte']
    return render(request,'drinks/index.html',{'drinks':drink_list})

def detail(request,drink_type):
    if drink_type == "mocha":
        description = "Our superior dark coffee made from beans from Arabia"
    elif drink_type == "espresso":
        description = "Our strong coffee brewed by forcing steam under pressure through darkly roasted, powdered coffee beans"
    else: 
        description = "Our coffee made with hot milk"
    return render(request,'drinks/detail.html',{'drink':drink_type,'drink_description':description})

