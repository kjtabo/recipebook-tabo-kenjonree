from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recipe
from .forms import RecipeForm


class RecipeCreateView(CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = "ledger/recipe_create.html"


class RecipeUpdateView(UpdateView):
    model = Recipe
    form_class = RecipeForm
    template_name = "ledger/recipe_detail.html"


class RecipeListView(ListView):
    model = Recipe
    template_name = "ledger/recipes_list.html"


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = "ledger/recipe_detail.html"
