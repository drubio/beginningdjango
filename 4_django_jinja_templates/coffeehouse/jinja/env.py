from jinja2.environment import Environment
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse
from coffeehouse.jinja.filters import customcoffee, squarerootintext, startswithvowel

class JinjaEnvironment(Environment):
    def __init__(self,**kwargs):
        super(JinjaEnvironment, self).__init__(**kwargs)
        self.globals['static'] = staticfiles_storage.url
        self.globals['url'] = reverse
        self.filters['customcoffee'] = customcoffee
        self.filters['squarerootintext'] = squarerootintext
        self.filters['startswithvowel'] = startswithvowel
        self.tests['startswithvowel'] = startswithvowel
