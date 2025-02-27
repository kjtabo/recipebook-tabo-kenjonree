from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Recipe, Ingredient


class RecipeListView(ListView):
    model = Recipe
    template_name = "ledger/recipes_list.html"


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "ledger/recipe_detail.html"


def recipe_detail(request, pk):
    recipe_detail = {
        "recipe": Ingredient.objects.filter(recipe__recipe__pk=pk)
    }
    return render(request, "ledger/recipe_detail.html", recipe_detail)


def index(request):
    return HttpResponse()
