from django.contrib import admin
from app1.models import Employee


# Register your models here.

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['EmpId', 'EmpName', 'EmpContact', 'EmpSal', 'EmpEmail', 'EmpAddress']
