from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Ingredients, Pizza
from .serializers import IngredientSerializer, PizzaSerializer


# Create your views here.

@api_view(["GET"])
def ingredients_list(request):
    """
    List all ingredients.
    """
    ingredients = Ingredients.objects.all()
    serializer = IngredientSerializer(ingredients, many=True)
    return Response(serializer.data)

@api_view(["POST"])
def ingredient_create(request):
    """
    Create a new ingredient.
    """
    serializer = IngredientSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(["GET"])
def pizzas_list(request):
    """
    List all pizzas.
    """
    pizzas = Pizza.objects.all()
    serializer = PizzaSerializer(pizzas, many=True)
    return Response(serializer.data)

@api_view(["POST"])
def pizza_create(request):
    """
    Create a new pizza.
    """
    serializer = PizzaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

