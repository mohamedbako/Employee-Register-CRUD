from django import forms
from .models import Employees

class EmployeeForms(forms.ModelForm):
    class Meta:
        model = Employees
        fields = '__all__'
        labels = {
            'fullName' : 'Full Name',
            'EmpCode' : 'EMP. Code'
        }
