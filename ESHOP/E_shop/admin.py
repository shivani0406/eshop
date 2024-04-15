from django.contrib import admin
from .models.products import Products
from .models.category import Catagories
from .models.customer import Customer
from .models.orders import Order



class AdminProducts(admin.ModelAdmin):
    list_display = ['name','price','category']

class AdminCategory(admin.ModelAdmin):
    list_display = ['name']    


admin.site.register(Products,AdminProducts)
admin.site.register(Catagories,AdminCategory)
admin.site.register(Customer)
admin.site.register(Order)

