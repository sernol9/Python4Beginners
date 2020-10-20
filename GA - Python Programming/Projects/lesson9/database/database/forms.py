from django import forms

from . import models


class OrderForm(forms.ModelForm):

    class Meta:
        model = models.Order
        fields = ('quantity',)

    def __init__(self, product, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.product = product

    def save(self, *args, **kwargs):
        order = super().save(commit=False, *args, **kwargs)
        order.product = self.product
        order.save()
        return order
