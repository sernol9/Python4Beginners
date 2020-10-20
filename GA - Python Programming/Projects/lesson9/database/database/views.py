from django.shortcuts import render, redirect,reverse

from . import models
from . import forms

def home_view(request):
    qs = models.Product.objects.all()
    ctx = {'qs': qs}
    return render(request, 'home_view.html', ctx)

def order_detail_view(request, order_id):
    order = models.Order.objects.get(id=order_id)
    ctx = {'order': order}
    return render(request, 'order_detail_view.html', ctx)

def product_detail_view(request, product_id):
    product = models.Product.objects.get(id=product_id)
    ctx = {'product': product}

    form = forms.OrderForm(product)

    if request.method == 'POST':
        form = forms.OrderForm(product,data=request.POST)
        if form.is_valid():
            order = form.save()
            ctx['order'] = order
            return redirect(reverse('order_detail_view',kwargs={'order_id' : order.id}))

    ctx['form'] = form
    return render(request, 'product_detail_view.html', ctx)



