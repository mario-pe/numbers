from django import forms
from django.core.validators import RegexValidator

numeric = RegexValidator(r'^[-0-9][0-9]*$', 'Only digits are allowed.')

class NumberForm(forms.Form):
    number = forms.CharField(label='number', max_length=13, validators=[numeric])