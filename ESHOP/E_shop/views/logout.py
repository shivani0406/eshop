from django.shortcuts import redirect
from django.views import View


class Logout(View):
    def get(self,request):
        request.session.clear()
        return redirect('login')