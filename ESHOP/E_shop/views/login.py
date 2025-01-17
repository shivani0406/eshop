from django.shortcuts import render,redirect
from E_shop.models.customer import Customer
from django.contrib.auth.hashers import check_password
from django.views import View





class Login(View):
    def get(self,request):
        return render(request,'orders/login.html')
    
    def post(self,request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None

        if customer:
            flag = check_password(password , customer.password)  

            if flag:
                request.session['customer'] = customer.id
                request.session['email'] = customer.email
                

                return redirect('index')
            else:
                error_message = 'Email or Password invalid...!'
        else:
            error_message = 'Email or Password invalid...!'
            # print(email,password)
            
        return render(request,'orders/login.html', {'error':error_message})    

    
  