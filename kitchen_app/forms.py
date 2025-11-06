from django import forms
from .models import DishType, Dish, Ingredient


class DishTypeForm(forms.ModelForm):
    class Meta:
        model = DishType
        fields = "__all__"

        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control form-control-lg border border-dark border-2 shadow-lg"}),
        }


class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = "__all__"

        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control form-control-lg border border-dark border-2 shadow-lg"}),
            "description": forms.TextInput(attrs={
                "class": "form-control form-control-lg border border-dark border-2 shadow-lg"}),
            "price": forms.TextInput(attrs={
                "class": "form-control form-control-lg border border-dark border-2 shadow-lg"}),
            "dish_type": forms.Select(attrs={
                "class": "form-control form-control-lg border border-dark border-2 shadow-lg"}),
            "ingredients": forms.CheckboxSelectMultiple(attrs={
                "class": "custom-checkbox-list border border-dark border-2 shadow-lg"},),
            "cooks": forms.SelectMultiple(attrs={
                "class": "custom-checkbox-list border border-dark border-2 shadow-lg"}),
        }


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = "__all__"

        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control form-control-lg border border-dark border-2 shadow-lg"}),
        }