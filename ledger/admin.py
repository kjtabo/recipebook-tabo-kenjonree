from django.contrib import admin
from .models import Recipe, Ingredient, RecipeIngredient, Profile

from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False


class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInline,]


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    verbose_name = "Recipe Ingredient"
    verbose_name_plural = "Recipe Ingredients"


class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [RecipeIngredientInline,]
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


admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
