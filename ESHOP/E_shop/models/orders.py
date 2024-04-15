from django.db import models
from E_shop.models import Products
from E_shop.models import Customer
import datetime


class Order(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=50 , default='',blank=True)
    phone = models.CharField(max_length=50 , default='',blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)


    def place_order(self):
        self.save()

    @staticmethod
    def get_customer_by_id(customer_id):
        return Order.objects.filter(customer = customer_id).order_by('-date')  