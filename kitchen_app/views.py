from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic

from .forms import (DishTypeForm,
                    DishForm,
                    IngredientForm,
                    CookCreationForm,
                    CookUpdateForm,
                    CookNameSearchForm,
                    IngredientNameSearchForm,
                    DishNameSearchForm)
from .models import Cook, DishType, Dish, Ingredient


def index(request):
    num_cooks = get_user_model().objects.all().count()
    num_dish_types = DishType.objects.all().count()
    num_dishes = Dish.objects.all().count()

    context = {
        'num_cooks': num_cooks,
        'num_dish_types': num_dish_types,
        'num_dishes': num_dishes,
    }

    return render(request, "kitchen_app/index.html", context=context)


class TypesOfDishesListView(generic.ListView):
    model = DishType
    template_name = "kitchen_app/dishtype_list.html"
    paginate_by = 8


class TypesOfDishesCreateView(LoginRequiredMixin, generic.CreateView):
    model = DishType
    form_class = DishTypeForm
    success_url = reverse_lazy("kitchen_app:dishtype-list")


class TypesOfDishesUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = DishType
    form_class = DishTypeForm
    success_url = reverse_lazy("kitchen_app:dishtype-list")


class TypesOfDishesDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = DishType
    success_url = reverse_lazy("kitchen_app:dishtype-list")


class DishesListView(generic.ListView):
    model = Dish
    template_name = "kitchen_app/dish_list.html"
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DishesListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name")
        context["search_form"] = DishNameSearchForm(
            initial={"name": name}
        )
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        form = DishNameSearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(
                name__icontains=form.cleaned_data["name"]
            )
        return queryset


class DishesDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dish

    def get_queryset(self):
        return super().get_queryset().prefetch_related("ingredients")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        dish_object = self.get_object()

        dish_ingredients = dish_object.ingredients.all()
        context["ingredients"] = dish_ingredients

        return context


class DishesCreateView(LoginRequiredMixin, generic.CreateView):
    model = Dish
    form_class = DishForm
    success_url = reverse_lazy("kitchen_app:dish-list")


class DishesUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Dish
    form_class = DishForm
    success_url = reverse_lazy("kitchen_app:dish-list")

    def get_success_url(self):
        dish_pk = self.object.pk

        return reverse("kitchen_app:dish-detail", kwargs={"pk": dish_pk})


class DishesDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Dish
    success_url = reverse_lazy("kitchen_app:dish-list")


class IngredientsListView(generic.ListView):
    model = Ingredient
    template_name = "kitchen_app/ingredient_list.html"
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IngredientsListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name")
        context["search_form"] = IngredientNameSearchForm(
            initial={"name": name}
        )
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        form = IngredientNameSearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(
                name__icontains=form.cleaned_data["name"]
            )
        return queryset


class IngredientsCreateView(LoginRequiredMixin, generic.CreateView):
    model = Ingredient
    form_class = IngredientForm
    success_url = reverse_lazy("kitchen_app:ingredient-list")


class IngredientsUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Ingredient
    form_class = IngredientForm
    success_url = reverse_lazy("kitchen_app:ingredient-list")


class IngredientsDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Ingredient
    success_url = reverse_lazy("kitchen_app:ingredient-list")


class CooksListView(generic.ListView):
    model = Cook
    paginate_by = 8

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CooksListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name")
        context["search_form"] = CookNameSearchForm(
            initial={"name": name}
        )
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        form = CookNameSearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(
                Q(first_name__icontains=form.cleaned_data["name"]) |
                Q(last_name__icontains=form.cleaned_data["name"]) |
                Q(username__icontains=form.cleaned_data["name"])
            )
        return queryset


class CooksDetailView(LoginRequiredMixin, generic.DetailView):
    model = Cook

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cook_object = self.get_object()

        cook_dishes = cook_object.dishes.all()
        context["cook_dishes"] = cook_dishes

        return context


class CooksCreateView(LoginRequiredMixin, generic.CreateView):
    model = Cook
    form_class = CookCreationForm
    success_url = reverse_lazy("kitchen_app:cook-list")


class CooksUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Cook
    form_class = CookUpdateForm

    def get_success_url(self):
        cook_pk = self.object.pk

        return reverse("kitchen_app:cook-detail", kwargs={"pk": cook_pk})


class CooksDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Cook
    success_url = reverse_lazy("kitchen_app:cook-list")
