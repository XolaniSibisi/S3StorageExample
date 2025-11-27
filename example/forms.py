from django import forms
from django.forms import widgets
from .models import Car


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ["name", "picture"]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "text-base p-2 border border-gray-300 rounded-lg focus:outline-none focus:border-indigo-500",
                    "placeholder": "Enter car name",
                }
            ),
            "picture": forms.ClearableFileInput(
                attrs={"class": "hidden"}  # keep hidden for the drag & drop UX
            ),
        }
