from django.db import models

# Create your models here.

class Pizza(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    tipo = models.CharField(max_length=10, choices=[('doce', 'Doce'), ('salgada', 'Salgada')])
    foto = models.ImageField(upload_to='pizzas/', null=True, blank=True)
    ingredientes = models.ManyToManyField('Ingredients', related_name='pizzas')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Ingredients(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
    