from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from .models import DishType, Dish, Ingredient, Cook


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


class CookCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = UserCreationForm.Meta.fields + (
            "years_of_experience",
            "first_name",
            "last_name",
        )

    def clean_years_of_experience(self):
        return validate_years_of_experience(self.cleaned_data["years_of_experience"])


class CookUpdateForm(forms.ModelForm):
    class Meta:
        model = Cook
        fields = ["years_of_experience", "first_name", "last_name"]


    def clean_years_of_experience(self):
        return validate_years_of_experience(self.cleaned_data["years_of_experience"])


def validate_years_of_experience(years_of_experience):
    if years_of_experience < 0:
        raise ValidationError("Years of experience must be greater or equal 0")


    return years_of_experience