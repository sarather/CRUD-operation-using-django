from cProfile import label
from django import forms
from .models import Employee


class EmployeeFrom(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('fullname', 'mobile', 'emp_code', 'position')
        labels = {
            'fullname': 'Full Name',
            'emp_code': 'Employee Code',
            'mobile': "Phone Number",

        }

    def __init__(self, *args, **kwargs):
        super(EmployeeFrom, self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Select Position"
        self.fields['emp_code'].required = False
