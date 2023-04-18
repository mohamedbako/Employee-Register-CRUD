from django.db import models

# Create your models here.

class Possition(models.Model):
    titie = models.CharField(max_length=50)

    def __str__(self):
        return self.titie

class Employees(models.Model):
    fullName = models.CharField(max_length=50)
    Mobile = models.CharField(max_length=50)
    EmpCode = models.CharField(max_length=50)
    Possition = models.ForeignKey(Possition, on_delete=models.CASCADE)

    
    