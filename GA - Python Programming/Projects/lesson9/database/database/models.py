from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=1024)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_published = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} (${self.price})'

class Order(models.Model):
    product = models.ForeignKey('database.Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
