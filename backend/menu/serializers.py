from rest_framework import serializers
from .models import Ingredients, Pizza

class PizzaSerializer(serializers.ModelSerializer):
    """
    Serializer for the Pizza model.
    """
    class Meta:
        model = Pizza
        fields = ['id', 'name', 'description', 'price', 'tipo', 'foto', 'ingredientes']


class IngredientSerializer(serializers.ModelSerializer):
    """
    Serializer for the Ingredients model.
    """
    class Meta:
        model = Ingredients
        fields = ['id', 'name', 'description']
