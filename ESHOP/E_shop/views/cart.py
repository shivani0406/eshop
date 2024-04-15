from django.shortcuts import render
from E_shop.models.products import Products


from django.views import View





class Cart(View):
    def get(self,request):
        ids = list(request.session.get('cart').keys())
        print(ids)
        products = Products.get_product_by_id(ids)
        print(products)
        return render(request,'cart.html',{'products':products})