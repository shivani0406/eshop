from django.shortcuts import render,redirect
from E_shop.models.customer import Customer
from django.contrib.auth.hashers import make_password
from django.views import View



class Signup(View):
    def get(self,request):
        return render(request,'signup.html')
    

    def post(self,request):
        postdata = request.POST
        first_name = postdata.get("firstname")               #signup page par jo name me value di hai wahi dena hai
        last_name = postdata.get("lastname")
        phone = postdata.get("phone")
        email = postdata.get("email")
        password = postdata.get("password")
        re_enter = postdata.get("re_enter")
        # print(first_name,last_name,phone,email,password)

        error_message = None

        customer = Customer(first_name = first_name,
                           last_name = last_name,
                           phone = phone,
                           email = email,
                           password = password,
                           re_enter = re_enter
                            )
        
        value = {
                    "first_name":first_name,
                    "last_name" : last_name,
                    "phone" : phone,
                    "email" : email
        }


        error_message =  self.Validate_Customer(customer)     
            
        if not error_message:
           customer = Customer(first_name=first_name,
                               last_name = last_name,
                               phone=phone,
                               email = email,
                               password=password,
                               re_enter=re_enter )
           customer.password = make_password(customer.password)
           customer.re_enter = make_password(customer.re_enter)
           customer.save()
           return redirect('index')
        else:  
         
            data = {'error': error_message,
                 'values': value}
        return render(request , "signup.html" , data) 

    
    def Validate_Customer(self,customer):
        #validations:   
        error_message = None
        
        if len(customer.password)<8:
            error_message = "password must be more than 8 character...! "
        elif (customer.re_enter != customer.password):
            error_message = "password is incorrect...!"
        if customer.isExist():
            error_message = "email address already registered...! "

        return  error_message   
