from django import forms
import re

class GenderField(forms.ChoiceField):
      def __init__(self, *args, **kwargs):
            super(GenderField, self).__init__(*args, **kwargs)
            self.error_messages = {"required":"Please select a gender, it's required"}
            self.choices = ((None,'Select gender'),('M','Male'),('F','Female'))

class PlaceholderInput(forms.widgets.Input):
      template_name = 'about/placeholder.html'
      input_type = 'text'
      def get_context(self, name, value, attrs):
            context = super(PlaceholderInput, self).get_context(name, value, attrs)
            context['widget']['attrs']['maxlength'] = 50
            context['widget']['attrs']['placeholder'] = name.title()
            return context    

    
def validate_comment_word_count(value):
      count = len(value.split())
      if count < 30:
            raise forms.ValidationError(('Please provide at least a 30 word message, %(count)s words is not descriptive enough'),
                                        params={'count': count},
            )
  
class ContactForm(forms.Form):
      name = forms.CharField(required=False,widget=PlaceholderInput)
      email = forms.EmailField(label='Your email',widget=PlaceholderInput)  
      comment = forms.CharField(widget=forms.Textarea,validators=[validate_comment_word_count],error_messages={"required":"Please, pretty please provide a comment"})
      gender = GenderField()
      field_order=['email','name','gender','comment']
      def __init__(self, *args, **kwargs):
            # Get 'initial' argument if any
            initial_arguments = kwargs.get('initial', None)
            updated_initial = initial_arguments
            if initial_arguments:
                  # We have initial arguments, fetch 'user' placeholder variable if any
                  user = initial_arguments.get('user',None)
                  # Now update the form's initial values if user
                  if user:
                        updated_initial['name'] = getattr(user, 'first_name', None)
                        updated_initial['email'] = getattr(user, 'email', None)
            # You can also initialize form fields with hardcoded values
            # or perform complex DB logic here to then perform initialization
            #updated_initial['comment'] = 'Please provide a comment'
            # Finally update the kwargs initial reference
            kwargs.update(initial=updated_initial)
            super(ContactForm, self).__init__(*args, **kwargs)
      def clean(self):
            # Call clean() method to ensure base class validation
            super(ContactForm, self).clean()
      	    # Get the field values from cleaned_data dict
            name = self.cleaned_data.get('name','')
            email = self.cleaned_data.get('email','')
            
            # Check if the name is part of the email
            if name.lower() not in email:
                  # Name is not in email , raise an error
                  message = "Please provide an email that contains your name, or viceversa"
                  #self.add_error('name', message)
                  #self.add_error('email', forms.ValidationError(message))
                  self.add_error(None, message)
                  #raise forms.ValidationError("Please provide an email that contains your name, or viceversa")            
      def clean_name(self):
            # Get the field value from cleaned_data dict
            value = self.cleaned_data['name']
            # Check if the value is all upper case
            if value.isupper():
                  # Value is all upper case, raise an error
                  raise forms.ValidationError("Please don't use all upper case for your name, use lower case",code='uppercase')
            # Always return value 
            return value
      def clean_email(self):
      	    # Get the field value from cleaned_data dict
            value = self.cleaned_data['email']
	    # Check if the value end in @hotmail.com
            if value.endswith('@hotmail.com'):
                  # Value ends in @hotmail.com, raise an error
                  raise forms.ValidationError("Please don't use a hotmail email, we simply don't like it",code='hotmail')
            # Always return value
            return value
