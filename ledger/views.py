from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recipe, RecipeImage
from .forms import RecipeForm, RecipeImageForm


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = "ledger/recipe_add.html"

    def get_context_data(self, **kwargs):
        ctx = super(RecipeCreateView, self).get_context_data(**kwargs)
        ctx["window"] = "Add a recipe"
        return ctx


class RecipeImageCreateView(CreateView):
    model = RecipeImage
    form_class = RecipeImageForm
    template_name = "ledger/recipe_add.html"

    def form_valid(self, form):
        form.instance.recipe = Recipe.objects.get(pk=self.kwargs["pk"])
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        ctx = super(RecipeImageCreateView, self).get_context_data(**kwargs)
        ctx["window"] = "Add an image"
        return ctx

    def get_success_url(self):
        return reverse_lazy(
            "ledger:recipe_detail",
            kwargs={"pk": self.kwargs["pk"]}
        )


class RecipeListView(ListView):
    model = Recipe
    template_name = "ledger/recipes_list.html"


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = "ledger/recipe_detail.html"

    def get_context_data(self, **kwargs):
        ctx = super(RecipeDetailView, self).get_context_data(**kwargs)
        ctx["pk"] = self.kwargs["pk"]
        return ctx
