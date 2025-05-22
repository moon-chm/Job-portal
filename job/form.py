from django import forms
from .models import companyAccount  ,EmployeeAccount

# company datd
class companyAccountForm(forms.ModelForm):
    class Meta:
        model = companyAccount
        fields =["dt_com_name","dt_com_mobile","dt_com_mail","dt_com_password","dt_com_address","dt_com_states","dt_com_logo","dt_com_informetion"]


# Employee data
class EmployeeAccountForm(forms.ModelForm):
    class Meta:
        model = EmployeeAccount
        fields = ["dt_emp_name", "dt_emp_mobile", "dt_emp_mail", "dt_emp_password", "dt_emp_address", "dt_emp_states", "dt_emp_college_name" ,"dt_emp_marks" ,"dt_emp_education", "dt_emp_field", "dt_emp_Resume", "dt_emp_Dp", "dt_emp_detelis"]  





