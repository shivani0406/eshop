"""
URL configuration for ESHOP project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from . import settings
from E_shop.views import home, signup, login, logout,cart, checkout, orders


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',home.Index.as_view(),name='index'),
    path('signup/',signup.Signup.as_view(),name='signup'),
    path('login/',login.Login.as_view(),name='login'),
    path('logout/',logout.Logout.as_view(),name='logout'),
    path('cart/',cart.Cart.as_view(),name='cart'),
    path('check-out/',checkout.CheckOut.as_view(),name='check-out'),
    path('orders/',orders.Orders_now.as_view(),name='orders'),





] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
