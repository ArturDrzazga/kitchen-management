from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .forms import DishTypeForm
from .models import Cook, DishType, Dish



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
    paginate_by = 5


class TypesOfDishesCreateView(generic.CreateView):
    model = DishType
    form_class = DishTypeForm
    success_url = reverse_lazy("kitchen_app:dishtype-list")


class TypesOfDishesUpdateView(generic.UpdateView):
    model = DishType
    form_class = DishTypeForm
    success_url = reverse_lazy("kitchen_app:dishtype-list")