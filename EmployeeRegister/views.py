from django.shortcuts import render

# Create your views here.


def employeeList(requset):
    return render(requset, 'EmployeeRegister/EmpList.html')

def employeeForm(requset):
    return render(requset, 'EmployeeRegister/EmpForm.html')

def employeeDelete(requset):
    pass