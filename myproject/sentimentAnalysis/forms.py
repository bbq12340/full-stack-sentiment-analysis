from django.db.models import fields
from .models import InputText
from django import forms


class InputTextForm(forms.ModelForm):
    class Meta:
        model = InputText
        fields = ['input_text']
