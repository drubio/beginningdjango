from django import template
register = template.Library()


@register.filter(is_safe=True)
def boldcoffee(value): # Only variable argument.    
    return '<b>%s</b>' % value

@register.filter(name='undercoffee',is_safe=True)
def undercoffee(value,arg="black"): # Variable argument and filter argument
    return '<u>%s</u>' % value
