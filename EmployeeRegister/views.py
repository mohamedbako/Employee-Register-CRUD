from django.shortcuts import render , redirect
from .forms import EmployeeForms
from .models import Employees
# Create your views here.


def employeeList(requset):
    context = {'EmpList': Employees.objects.all()}
    return render(requset, 'EmployeeRegister/EmpList.html', context)

def employeeForm(request):
    if request.method == 'GET':
        form = EmployeeForms()
        return render(request, 'EmployeeRegister/EmpForm.html', {'form': form})
    else:
        form = EmployeeForms(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/employee/list')
def employeeDelete(requset):
    pass