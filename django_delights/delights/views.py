from django.shortcuts import render
from .models import Ingredient, Purchase, MenuItem
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import Http404, HttpResponse, HttpRequest

# Create your views here.

def home_view(request):
    return render(request, "delights/base.html")

class getIngredientCollection(ListView):
    model = Ingredient
    template_name = "delights/IngredientsCollection.html"
    #fields = [""]

class getPurchaseList(ListView):
    model = Purchase
    template_name = "delights/PurchaseList.html"

class getMenuList(ListView):
    model = MenuItem
    template_name = "delights/MenuList.html"
