from django.shortcuts import render
from .models import Client, Order
from .serializers import ClientsSerializer, OrdersSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.
    
@api_view(["GET"])
def clients_list(request):
    """
    List all clients.
    """
    clients = Client.objects.all()
    serializer = ClientsSerializer(clients, many=True)
    return Response(serializer.data)

@api_view(["POST"])
def client_create(request):
    """
    Create a new client.
    """
    serializer = ClientsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(["GET"])
def orders_list(request):
    """
    List all orders.
    """
    clients = Order.objects.all()
    serializer = OrdersSerializer(clients, many=True)
    return Response(serializer.data)

@api_view(["POST"])
def order_create(request):
    """
    Create a new order.
    """
    serializer = OrdersSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

