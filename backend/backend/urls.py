"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from pizzaria.views import hello_world
from menu.views import ingredients_list, ingredient_create, pizzas_list, pizza_create
from clients.views import orders_list, order_create, clients_list, client_create

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/hello/", hello_world),
    path('api/ingredients/', ingredients_list, name='ingredient-list'),
    path('api/ingredients/create/', ingredient_create, name='ingredient-create'),
    path('api/pizzas/', pizzas_list, name='pizza-list'),
    path('api/pizzas/create/', pizza_create, name='pizza-create'),
    path('api/orders/', orders_list, name='order-list'),
    path('api/orders/create/', order_create, name='order-create'),
    path('api/clients/', clients_list, name='client-list'),
    path('api/clients/create/', client_create, name='client-create'),
]
