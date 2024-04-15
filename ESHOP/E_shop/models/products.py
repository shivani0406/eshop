from django.db import models
from .category import Catagories


class Products(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    description = models.TextField(max_length=200,default='')
    image = models.ImageField(upload_to='uploads/products/')
    category = models.ForeignKey(Catagories,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    class Meta:
        db_table = 'products'

    @staticmethod
    def get_all_products():
        return  Products.objects.all()  

    @staticmethod
    def get_all_products_by_category_id(category_id):
        if category_id:
            return Products.objects.filter(category=category_id) 
        else:
           return Products.get_all_products()  
  
    @staticmethod
    def get_product_by_id(ids):
        return Products.objects.filter(id__in = ids)