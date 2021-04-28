from django.forms import ModelForm, DateInput

from .models import Employee


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        widgets = {
            'birth_date': DateInput(attrs={'type': 'date'}),
            'hire_date': DateInput(attrs={'type': 'date'}),
        }
