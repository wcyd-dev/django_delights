from django.shortcuts import render
from .models import Ingredient, Purchase, MenuItem, RecipeRequirement
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import Http404, HttpResponse, HttpRequest
from django.urls import reverse_lazy

# Create your views here.

def home_view(request):
    #calculate total revenue
    allPurchases = Purchase.objects.all()
    revenue = 0
    cost = 0
    for purchase in allPurchases:
        revenue += purchase.menu_item.price

        recipeRequirements = RecipeRequirement.objects.filter(menu_item=purchase.menu_item)
        for requirement in recipeRequirements:
            ingredient = requirement.ingredient
            cost_to_make = requirement.quantity * ingredient.unit_price
            cost += cost_to_make

    revenue = round(revenue,2)
    cost = round(cost,2)
    profit = revenue - cost
    profit = round(profit,2)
    return render(request, "delights/home.html", {"revenue": revenue, "cost": cost, "profit": profit})

class getIngredientCollection(ListView):
    model = Ingredient
    template_name = "delights/IngredientList.html"
    #fields = [""]

class getPurchaseList(ListView):
    model = Purchase
    template_name = "delights/PurchaseList.html"

class getMenuList(ListView):
    model = MenuItem
    template_name = "delights/MenuList.html"

    def get_queryset(self):
        return MenuItem.objects.prefetch_related('reciperequirement_set__ingredient')

class getRecipeList(ListView):
    model = RecipeRequirement
    template_name = "delights/RecipeList.html"

class createIngredient(CreateView):
    model = Ingredient
    template_name = "delights/create_ingredient_form.html"
    fields = ["name","unit_price","quantity","unit"]
    
class updateIngredient(UpdateView):
    model = Ingredient
    template_name = "delights/update_ingredient_form.html"
    fields = ["name","unit_price","quantity","unit"]
    success_url = reverse_lazy("ingredient_list")

class deleteIngredient(DeleteView):
    model = Ingredient
    template_name = "delights/delete_ingredient_form.html"
    success_url = reverse_lazy("ingredient_list")
