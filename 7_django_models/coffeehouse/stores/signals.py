# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models.signals import pre_init, post_init
from django.dispatch import receiver, Signal


import logging

stdlogger = logging.getLogger(__name__)

@receiver(pre_init, sender='stores.Store')
def run_before_init(sender, **kwargs):
    stdlogger.info("Start pre_init Store in signals.py under stores app")
    stdlogger.info("sender %s" % (sender))
    stdlogger.info("kwargs %s" % str(kwargs))

@receiver(post_init, sender='stores.Store')
def run_after_init(sender, **kwargs):
    stdlogger.info("Start post_init Store in signals.py under stores app")
    stdlogger.info("sender %s" % (sender))
    stdlogger.info("kwargs %s" % str(kwargs))

store_closed = Signal(providing_args=["employee"])   


@receiver(store_closed)
def run_when_store_is_closed(sender,**kwargs):
    stdlogger.info("Start store_closed Store in signals.py under stores app")
    stdlogger.info("sender %s" % (sender))
    stdlogger.info("kwargs %s" % str(kwargs))

