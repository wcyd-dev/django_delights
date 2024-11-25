from django.db import models
from datetime import datetime

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    unit_price = models.FloatField()
    quantity = models.FloatField()
    unit = models.CharField(max_length=100)

    class Meta: 
        verbose_name_plural = 'Ingredients'
        ordering = ["name"]

    def get_absolute_url(self):
        return "list"

class MenuItem(models.Model):
    title = models.CharField(max_length=150)
    price = models.FloatField()

    class Meta: 
        verbose_name_plural = 'Menu Items'
        ordering = ["title"]

class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=datetime.now)

class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem,on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.SET_NULL, null=True)
    quantity = models.FloatField()
