from django.shortcuts import render
from django import forms

from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from django.contrib.messages.views import SuccessMessageMixin

from django.http import HttpResponseRedirect

class UserSignupForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        

class UserSignUp(SuccessMessageMixin,CreateView):
    model = User
    form_class = UserSignupForm
    success_url = reverse_lazy('items:index')
    success_message = "User created successfully"
    template_name = "registration/signup.html"
    def form_valid(self, form):
        super(UserSignUp,self).form_valid(form)        
        # The form is valid, automatically sign-in the user
        user = authenticate(self.request, username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
        if user == None:
            # User not validated for some reason, return standard form_valid() response
            return self.render_to_response(self.get_context_data(form=form))            
        else:
            # Log the user in
            login(self.request, user)
            # Redirect to success url
            return HttpResponseRedirect(self.get_success_url())            

