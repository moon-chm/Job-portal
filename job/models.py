from django.db import models

# Create your models here.

# Company Account Data
class companyAccount(models.Model):
    dt_com_name = models.CharField( max_length=120)
    dt_com_mobile = models.CharField( max_length=120)
    dt_com_mail = models.CharField( max_length=120)
    dt_com_password = models.CharField( max_length=120)
    dt_com_address = models.TextField()
    dt_com_states = models.CharField( max_length=120)
    dt_com_logo = models.ImageField(upload_to='Company_Logo/',max_length=300)
    dt_com_informetion = models.TextField()

    def __str__(self) :
        return self.dt_com_name
    

# Emp Account Data
class EmployeeAccount(models.Model):
    dt_emp_name = models.CharField( max_length=120)
    dt_emp_mobile = models.CharField( max_length=120)
    dt_emp_mail = models.CharField( max_length=120)
    dt_emp_password = models.CharField( max_length=120)
    dt_emp_address = models.CharField( max_length=120)
    dt_emp_states = models.CharField( max_length=120)
    dt_emp_college_name = models.CharField( max_length=120)
    dt_emp_marks = models.CharField(max_length=120)
    dt_emp_education = models.CharField( max_length=120)
    dt_emp_field = models.CharField( max_length=120)
    dt_emp_Resume  = models.FileField( upload_to = 'Employee_Resume/',max_length=300)
    dt_emp_Dp  = models.ImageField( upload_to = 'Employee_DP/',max_length=300)
    dt_emp_detelis = models.TextField( max_length=800)

    def __str__(self) :
        return self.dt_emp_name



# Company Jop Post data
class CreatePost(models.Model):
    c_Post_id = models.CharField( max_length=120 )
    c_company_id = models.CharField( max_length=120)
    c_com_name = models.CharField( max_length=120)
    c_job_title = models.CharField( max_length=120)
    c_job_com_logo = models.CharField( max_length=120)
    c_joblpg = models.CharField( max_length=120)
    c_job_state = models.CharField( max_length=120)
    c_job_pincode = models.CharField( max_length=120)
    c_job_deteils = models.CharField( max_length=220)
    c_job_recruitment = models.CharField( max_length=220)

    def __str__(self) :
        return self.c_job_title
    

#Job post apply
class EmpJobPost(models.Model):
    jp_Post_id = models.CharField( max_length=120)
    jp_Com_id = models.CharField( max_length=120)
    jp_emp_id = models.CharField( max_length=120)
    jp_emp_Dp = models.CharField( max_length=120)
    jp_emp_name = models.CharField( max_length=120)
    jp_emp_info = models.CharField( max_length=120)
    jp_emp_status = models.CharField( max_length=120)
    jp_com_name = models.CharField( max_length=120)
    jp_job_title = models.CharField( max_length=120)
    jp_job_com_logo = models.CharField( max_length=120)
    jp_joblpg = models.CharField( max_length=120)
    jp_job_state = models.CharField( max_length=120)
    jp_job_pincode = models.CharField( max_length=120)
    jp_job_deteils = models.CharField( max_length=220)
    jp_job_recruitment = models.CharField( max_length=220)
    

    def __str__(self) :
        return self.jp_emp_name

