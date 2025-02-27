from django.contrib import admin
from .models import Recipe, Ingredient, RecipeIngredient


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient


class RecipeIngredientAdmin(admin.ModelAdmin):
    model = RecipeIngredient
    fieldsets = (
        ("Recipe and Ingredient Information", {
            "fields": (
                "quantity", ("ingredient", "recipe")
            ),
        }),
    )


class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [RecipeIngredientInline,]
    fieldsets = (
        ("Recipe Information", {
            "fields": (
                "name",
            ),
        }),
    )


class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient
    fieldsets = (
        ("Ingredient Information", {
            "fields": (
                "name",
            ),
        }),
    )


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
