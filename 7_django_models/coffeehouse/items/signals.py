# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models.signals import pre_save
from django.dispatch import receiver


import logging

stdlogger = logging.getLogger(__name__)

@receiver(pre_save, sender='items.Item')
def run_before_saving(sender, **kwargs):
    stdlogger.info("Start pre_save Item in signals.py under items app")
    stdlogger.info("sender %s" % (sender))
    stdlogger.info("kwargs %s" % str(kwargs))
