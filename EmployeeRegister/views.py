from django.shortcuts import render
from .forms import EmployeeForms
# Create your views here.


def employeeList(requset):
    return render(requset, 'EmployeeRegister/EmpList.html')

def employeeForm(request):
    form = EmployeeForms()
    return render(request, 'EmployeeRegister/EmpForm.html', {'form': form})

def employeeDelete(requset):
    pass