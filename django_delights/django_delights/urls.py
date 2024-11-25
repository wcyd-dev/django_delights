"""
URL configuration for django_delights project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from delights import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_view, name="home"),
    path('ingredient/list', views.getIngredientCollection.as_view(), name="ingredient_list"),
    path('purchase/list', views.getPurchaseList.as_view(), name="purchase_list"),
    path('menu/list', views.getMenuList.as_view(), name="menu_list"),
    path('recipe/list', views.getRecipeList.as_view(), name="recipe_list"),
]
