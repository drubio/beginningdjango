# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from jinja2 import lexer, nodes
from jinja2.ext import Extension
from django.utils import timezone
from django.template.defaultfilters import date
from django.conf import settings
from datetime import datetime


class DjangoNow(Extension):
    """
    Implements django's '{% now %}' tag:
        Today is : {% now "F jS o" %}
        {% now "F jS o" as today %}
        Today is today: {{ today }}
    """
    tags = set(['now'])

    def _now(self, date_format):
        tzinfo = timezone.get_current_timezone() if settings.USE_TZ else None
        formatted = date(datetime.now(tz=tzinfo),date_format)
        return formatted


    def parse(self, parser):
        lineno = next(parser.stream).lineno
        token = parser.stream.expect(lexer.TOKEN_STRING)
        date_format = nodes.Const(token.value)
        call = self.call_method('_now', [date_format], lineno=lineno)
        token = parser.stream.current
        if token.test('name:as'):
            next(parser.stream)
            as_var = parser.stream.expect(lexer.TOKEN_NAME)
            as_var = nodes.Name(as_var.value, 'store', lineno=as_var.lineno)
            return nodes.Assign(as_var, call, lineno=lineno)
        else:
            return nodes.Output([call], lineno=lineno)
