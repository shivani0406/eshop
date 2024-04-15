from django.shortcuts import render , redirect
from E_shop.models.products import Products
from E_shop.models.category import Catagories
from django.views import View

# Create your views here.

class Index(View):
    def get(self,request):
        products = None
        categories =Catagories.get_all_catagories()
        categoryID = request.GET.get('category')
        if categoryID:
            products=Products.get_all_products_by_category_id(categoryID)
        else:
            products=Products.objects.all()    
        data={}
        data['products'] = products
        data['categories'] = categories
        # print("you are :" , request.session.get('email'))
        return render(request,'orders/index.html',data)
   
    
    def post(self,request):
        # request.session.clear()
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity == 1:
                        cart.pop(product)
                    else:    
                        cart[product] = quantity-1
                else:
                    cart[product] = quantity+1    
            else:
                cart[product] = 1    
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart  
        print("you are :" , request.session.get('email')) 
        print( request.session['cart'])     
        # print(product)
        return redirect('index')

    








