from django.shortcuts import render
from E_shop.models.orders import Order
from E_shop.middlewares.auth import auth_middleware
from django.utils.decorators import method_decorator


from django.views import View





class Orders_now(View):

    @method_decorator(auth_middleware)
    def get(self,request):
        customer = request.session.get('customer')
        orders = Order.get_customer_by_id(customer)
        print(orders)
        return render(request, 'orders.html',{'orders':orders})
       