from django import forms
from .models import Employees

class EmployeeForms(forms.ModelForm):
    class Meta:
        model = Employees
        fields = '__all__'
