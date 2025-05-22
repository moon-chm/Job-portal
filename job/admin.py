from django.contrib import admin
from job.models import companyAccount  ,EmployeeAccount, CreatePost, EmpJobPost


# Register your models here.
admin.site.register(companyAccount)

admin.site.register(EmployeeAccount)

admin.site.register(CreatePost)

admin.site.register(EmpJobPost)