from rest_framework import serializers
from .models import Client, Order, Pizza

class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name', 'email', 'phone', 'address', 'created_at', 'updated_at']

class OrdersSerializer(serializers.ModelSerializer):
    pizzas = serializers.PrimaryKeyRelatedField(many=True, queryset=Pizza.objects.all())

    class Meta:
        model = Order
        fields = ['id', 'cliente', 'endereco', 'telefone', 'pizzas', 'status', 'created_at', 'updated_at']

