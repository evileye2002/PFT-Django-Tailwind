from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from .models import Transaction, TransactionType, Category

User = get_user_model()


class TransactionForm(forms.ModelForm):
    type = forms.ChoiceField(required=False, choices=TransactionType.choices)
    date = forms.DateField(input_formats=["%d-%m-%Y"])

    class Meta:
        model = Transaction
        fields = ["name", "type", "category", "amount", "date", "description"]


class CategoryForm(forms.ModelForm):
    type = forms.ChoiceField(required=False, choices=TransactionType.choices)

    class Meta:
        model = Category
        fields = ["name", "type", "description"]
