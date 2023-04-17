from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.employeeForm),
    path('list/', views.employeeList),
]
