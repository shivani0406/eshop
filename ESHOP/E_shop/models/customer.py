from django.db import models



class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=13)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=500)
    re_enter = models.CharField(max_length=500, null=True)


    def __str__(self):
        return self.first_name
    
    class Meta:
        db_table = 'customer'

    def isExist(self):
        if Customer.objects.filter(email=self.email) :
            return True
        return False   
        
    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email = email)
        except:
            return False    