from distutils.util import strtobool
from django_filters import rest_framework as filters
from .models import Favorite, Recipe, ShoppingCart, Tag


CHOICES = (
    ('0', 'False'),
    ('1', 'True')
)


class RecipeFilter(filters.FilterSet):
    is_favorited = filters.ChoiceFilter(
        choices=CHOICES,
        method='is_favorited_method'
    )
    is_in_shopping_cart = filters.ChoiceFilter(
        choices=CHOICES,
        method='is_in_shopping_cart_method'
    )
    author = filters.NumberFilter(
        field_name='author',
        lookup_expr='exact'
    )
    tags = filters.ModelMultipleChoiceFilter(
        field_name='tags__slug',
        to_field_name='slug',
        queryset=Tag.objects.all()
    )

    def is_favorited_method(self, queryset, name, value):
        if self.request.user.is_anonymous:
            return Recipe.objects.none()

        favorites = Favorite.objects.filter(user=self.request.user)
        recipes = [item.recipe.id for item in favorites]
        new_queryset = queryset.filter(id__in=recipes)

        if not strtobool(value):
            return queryset.difference(new_queryset)

        return queryset.filter(id__in=recipes)

    def is_in_shopping_cart_method(self, queryset, name, value):
        if self.request.user.is_anonymous:
            return Recipe.objects.none()

        shopping_cart = ShoppingCart.objects.filter(user=self.request.user)
        recipes = [item.recipe.id for item in shopping_cart]
        new_queryset = queryset.filter(id__in=recipes)

        if not strtobool(value):
            return queryset.difference(new_queryset)

        return queryset.filter(id__in=recipes)

    class Meta:
        model = Recipe
        fields = ('author', 'tags')
