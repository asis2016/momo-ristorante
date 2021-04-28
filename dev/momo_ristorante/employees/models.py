"""
    employees/models.py
    -------------------
    An employee is a part of the company.
    The employee can post a blog, create a recipe, and view the dashboard.
    Each employee can update their profile.
"""
from django.db import models


class Employee(models.Model):
    """ Employee model as of v.1.0 """
    EMPLOYEE_TYPE = (
        ('chef', 'Chef'),
        ('waiter', 'Waiter'),
        ('bartender', 'Bartender'),
        ('kitchen_assistant', 'Kitchen Assistant'),
        ('manager', 'Manager'),
        ('helper', 'Helper'),
        ('author', 'Author'),
    )

    GENDER = (
        ('M', 'Male'),
        ('F', 'Female')
    )

    id = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=50)
    birth_date = models.DateField(blank=True)
    gender = models.CharField(choices=GENDER, default='M', max_length=6)
    hire_date = models.DateField(blank=True)
    type = models.CharField(choices=EMPLOYEE_TYPE, default='helper', max_length=20)

    def __str__(self):
        return str(self.name)
