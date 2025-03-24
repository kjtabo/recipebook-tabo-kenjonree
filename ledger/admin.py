from django.contrib import admin
from .models import Recipe, Ingredient, RecipeIngredient, RecipeImage


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    verbose_name = "Recipe Ingredient"
    verbose_name_plural = "Recipe Ingredients"


class RecipeImageInline(admin.TabularInline):
    model = RecipeImage
    verbose_name = "Recipe Image"
    verbose_name_plural = "Recipe Images"


class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [RecipeIngredientInline, RecipeImageInline,]
    list_display = ("name", "created_on", "updated_on")
    fieldsets = (
        ("Recipe Information", {
            "fields": (
                "name", "author",
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
