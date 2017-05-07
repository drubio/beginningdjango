from django.shortcuts import render
from coffeehouse.drinks.forms import DrinkForm,BaseDrinkFormSet
from django.forms import formset_factory
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    extra_forms = 2
    DrinkFormSet = formset_factory(DrinkForm, formset=BaseDrinkFormSet, extra=extra_forms, max_num=20)
    if request.method == 'POST':
        if 'additems' in request.POST and request.POST['additems'] == 'true':
            formset_dictionary_copy = request.POST.copy()
            formset_dictionary_copy['form-TOTAL_FORMS'] = int(formset_dictionary_copy['form-TOTAL_FORMS']) + extra_forms
            formset = DrinkFormSet(formset_dictionary_copy)
        else:
            formset = DrinkFormSet(request.POST)
            if formset.is_valid():
                return HttpResponseRedirect('/about/contact/thankyou')
    else:
        formset = DrinkFormSet(initial=[{'name': 1,'size': 'm','amount':1}])
    return render(request,'online/index.html',{'formset':formset})
