from django import forms

from .models import Recipe, RecipeImage


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        # fields = ["name"]
        fields = "__all__"


class RecipeImageForm(forms.ModelForm):
    class Meta:
        model = RecipeImage
        fields = ["image", "description"]
        # fields = "__all__"
