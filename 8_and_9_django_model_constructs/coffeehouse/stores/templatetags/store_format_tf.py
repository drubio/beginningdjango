# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import template
from django.utils.html import escape
from django.utils.safestring import mark_safe


register = template.Library()


@register.filter(is_safe=True)
def boldcoffee(value): 
    '''Returns input wrapped in HTML <b> tags'''
    return '<b>%s</b>' % value

@register.filter(needs_autoescape=True)
def smartcoffee(value, autoescape=True):
    '''Returns input wrapped in HTML <b> tags'''
    '''and also detects surrounding autoescape on filter (if any) and escapes '''
    if autoescape:
        value = escape(value)
    result = '<b>%s</b>' % value
    return mark_safe(result)


@register.filter(name='customcoffee',is_safe=True)
def coffee(value,arg="muted"): 
    '''Returns input wrapped in HTML <span> tags with a CSS class'''
    '''Defaults to CSS class 'muted' from Bootstrap'''
    return '<span class="%s">%s</span>' % (arg,value)

