# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models

from django.core.exceptions import ValidationError

def validate_comment_word_count(value):
      count = len(value.split())
      if count < 30:
            raise ValidationError(('Please provide at least a 30 word message, %(count)s words is not descriptive enough'),
                                        params={'count': count},
            )

@python_2_unicode_compatible
class Contact(models.Model):
      name = models.CharField(max_length=50,blank=True)
      email = models.EmailField()  
      comment = models.CharField(max_length=1000,validators=[validate_comment_word_count])
      def __str__(self):
            return "%s" % (self.name)
      
