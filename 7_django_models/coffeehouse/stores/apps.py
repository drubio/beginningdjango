# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class StoresConfig(AppConfig):
    name = 'coffeehouse.stores'

    def ready(self):
        import coffeehouse.stores.signals
