from django.shortcuts import render , redirect
from .forms import EmployeeForms
from .models import Employees
# Create your views here.


def employeeList(requset):
    context = {'EmpList': Employees.objects.all()}
    return render(requset, 'EmployeeRegister/EmpList.html', context)

def employeeForm(request, id = 0):
    if request.method == 'GET':
        if id == 0:
            form = EmployeeForms()
        else:
            employee = Employees.objects.get(pk = id)
            form = EmployeeForms(instance = employee)
        return render(request, 'EmployeeRegister/EmpForm.html', {'form': form})
    else:
        if id == 0:
            form = EmployeeForms(request.POST)
        else:
            employee = Employees.objects.get(pk = id)
            form = EmployeeForms(request.POST, instance = employee)
        if form.is_valid():
            form.save()
        return redirect('/employee/list')
    

def employeeDelete(requset, id):
    employee = Employees.objects.get(pk = id)
    employee.delete()
    return redirect('/employee/list')
