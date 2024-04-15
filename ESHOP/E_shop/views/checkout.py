from django.shortcuts import redirect
from E_shop.models.products import Products
from E_shop.models.orders import Order
from E_shop.models.customer import Customer




from django.views import View





class CheckOut(View):
    def post(self,request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Products.get_product_by_id(cart.keys())
        print(address, phone, customer, cart, products)

        for product in products:
            order = Order(customer = Customer(id=customer),
                          product = product,
                          price = product.price,
                          address = address,
                          phone = phone,
                          quantity = cart.get(str(product.id)) )
            order.place_order()
            request.session['cart'] = {}
        return redirect('cart')