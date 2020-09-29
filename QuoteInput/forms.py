from django import forms
from .models import QuoteInputModel


class QuoteInputForm(forms.ModelForm):
    class Meta:
        model = QuoteInputModel
        fields = '__all__'
