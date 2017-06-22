# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from django import forms


@python_2_unicode_compatible
class SharingFile(models.Model):
    file = models.FileField(upload_to='.')
    def __str__():
        return "%s" % (self.file)    
    
class SharingForm(forms.ModelForm):
    class Meta:      
        model = SharingFile
        fields = '__all__'    
        labels = {
            "file": "Photo / Video"
        }
