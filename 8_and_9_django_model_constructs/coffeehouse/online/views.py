from django.shortcuts import render
from django.forms import modelformset_factory
from django.http import HttpResponseRedirect
from .models import Order,OrderItem, OrderItem, OrderItemForm,BaseItemFormSet

#
# Create your views here.
def index(request):
    extra_forms = 2
    OrderSet = modelformset_factory(OrderItem,formset=BaseItemFormSet, form=OrderItemForm, fields=['item','amount'],extra=extra_forms, max_num=20)
    if request.method == 'POST':
        if 'additems' in request.POST and request.POST['additems'] == 'true':
            formset_dictionary_copy = request.POST.copy()
            formset_dictionary_copy['form-TOTAL_FORMS'] = int(formset_dictionary_copy['form-TOTAL_FORMS']) + extra_forms
            formset = OrderSet(formset_dictionary_copy)
        else:
            formset = OrderSet(request.POST)
            if formset.is_valid():
                # Generate new order
                new_order = Order()
                new_order.save()
                order_items = formset.save(commit=False)
                for order_item in order_items:
                    order_item.order = new_order
                    order_item.save()
                return HttpResponseRedirect('/about/contact/thankyou')
    else:
        formset = OrderSet(queryset=OrderItem.objects.none())
    return render(request,'online/index.html',{'formset':formset})
