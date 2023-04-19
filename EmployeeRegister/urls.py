from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.employeeForm, name= 'EmpInsert'),
    path('/<int:id>', views.employeeForm, name= 'EmpEdit'),
    path('list/', views.employeeList, name= 'EmpList'),
]
