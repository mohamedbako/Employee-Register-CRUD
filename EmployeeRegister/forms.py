from django import forms
from .models import Employees

class EmployeeForms(forms.ModelForm):
    class Meta:
        model = Employees
        fields = {'fullName', 'Mobile', 'EmpCode', 'Possition'}
        labels = {
            'fullName' : 'Full Name',
            'EmpCode' : 'EMP. Code'
        }
        widgets = {
            'Possition': forms.Select( attrs={'class': 'form-control'})
        }
# To set 'Select' as first select in position dropdown
    def __init__(self, *args, **kwargs):
        super(EmployeeForms, self).__init__(*args, **kwargs)
        self.fields['Possition'].empty_label = 'Select'
