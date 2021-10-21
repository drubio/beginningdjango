# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import jinja2

def customcoffee(value,arg="muted"):
    '''Returns input wrapped in HTML <span> tags with a CSS class'''
    '''Defaults to CSS class 'muted' from Bootstrap'''
    return jinja2.Markup('<span class="%s">%s</span>' % (arg,value))

import math
def squarerootintext(value):
    '''Returns square root in text'''
    return "The square root of %s is %s" % (value,math.sqrt(value))

def startswithvowel(value):
    '''Tests if a value starts with a vowel'''
    if value.lower().startswith(("a", "e", "i", "o","u")):
        return True
    else:
        return False
