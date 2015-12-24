from jinja2.environment import Environment
from django.conf import settings
from coffeehouse.jinja.filters import customcoffee, squarerootintext, startswithvowel

class JinjaEnvironment(Environment):
    def __init__(self,**kwargs):
        super(JinjaEnvironment, self).__init__(**kwargs)
        self.globals['STATIC_URL'] = settings.STATIC_URL
        self.filters['customcoffee'] = customcoffee
        self.filters['squarerootintext'] = squarerootintext
        self.filters['startswithvowel'] = startswithvowel
        self.tests['startswithvowel'] = startswithvowel
