from django import forms

DRINKS = ((None,'Please select a drink type'),(1,'Mocha'),(2,'Espresso'),(3,'Latte'))
SIZES = ((None,'Please select a drink size'),('s','Small'),('m','Medium'),('l','Large'))

from django.forms import BaseFormSet


class BaseDrinkFormSet(BaseFormSet):
    def clean(self):
        # Check errors dictionary first, if there are any error, no point in validating further
        if any(self.errors):
            return
        name_size_tuples = []
        for form in self.forms:
            name_size = (form.cleaned_data['name'],form.cleaned_data['size'])
            if name_size in name_size_tuples:
                raise forms.ValidationError("Ups! You have multiple %s %s items in your order, keep one and increase the amount" % (dict(SIZES)[name_size[1]],dict(DRINKS)[int(name_size[0])]))
            name_size_tuples.append(name_size)


class DrinkForm(forms.Form):
    name = forms.ChoiceField(choices=DRINKS,initial=0)
    size = forms.ChoiceField(choices=SIZES,initial=0)
    amount = forms.ChoiceField(choices=[(None,'Amount of drinks')]+[(i, i) for i in range(1,10)])    
