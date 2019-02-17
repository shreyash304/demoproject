"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path,include
from shop101.views import test,products_list,cart,delete_cart_item,show_product


urlpatterns = [
    path('test/', test),
    path('product/<id>',show_product),
    path('cart/',cart),
    path('cart/delete/', delete_cart_item),
    path('', products_list),
    path('admin/', admin.site.urls),
    path('user/', include('django.contrib.auth.urls'))
]
