from django.contrib import admin
from mysite.models import employee,task
# Register your models here.
class taskadmin(admin.ModelAdmin):
    fields=["id","employee_id","employee_name","task_title","task_end_date","upload_task"]
    
class employeeadmin(admin.ModelAdmin):
    fields=["employee_id","department_name","employee_name","employee_email","employee_address","employee_doj","profile"]
    
admin.site.register(employee,employeeadmin)
admin.site.register(task,taskadmin)

    