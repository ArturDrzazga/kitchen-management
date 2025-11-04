from django import forms
from .models import DishType

class DishTypeForm(forms.ModelForm):
    class Meta:
        model = DishType
        fields = "__all__"

        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control form-control-lg border border-dark border-2 shadow-lg"}),
        }
