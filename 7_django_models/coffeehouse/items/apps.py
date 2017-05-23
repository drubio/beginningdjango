# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class ItemsConfig(AppConfig):
    name = 'coffeehouse.items'
    
    def ready(self):
        import coffeehouse.items.signals
