from email.policy import default
from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.

    
class employee(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    employee_id=models.IntegerField()
    department_name=models.CharField(max_length=30)
    employee_name=models.CharField(max_length=30)
    employee_email=models.CharField(max_length=30)
    employee_address=models.CharField(max_length=30)
    employee_doj=models.CharField(max_length=30)
    profile=models.ImageField()
    status=models.BooleanField(default=False)
    added_on =models.DateTimeField(auto_now_add=True,null=True)
    update_on = models.DateTimeField(auto_now=True,null=True)
    def __str__(self):
        return self.user.username
    
class task(models.Model):
    id=models.IntegerField(primary_key=True)
    employee_id=models.CharField(max_length=30)
    employee_name=models.CharField(max_length=30)
    task_title=models.CharField(max_length=30)
    task_end_date=models.CharField(max_length=30)
    upload_task=models.FileField()