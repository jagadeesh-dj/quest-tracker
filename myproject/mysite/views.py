from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from .models import employee,task
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import datetime
# Create your views here.
def home(request):
    return render(request,"home.html")

def register(request):
    if "user_id"in request.COOKIES:
        uid = request.COOKIES["user_id"]
        usr = get_object_or_404(User,id=uid)
        login(request,usr)
        if usr.is_superuser:
            return HttpResponseRedirect("/admin")
        if usr.is_active:
            return HttpResponseRedirect("/userhome")
    if request.method=='POST':
        name=request.POST["uname"]
        empid=request.POST["employeeid"]
        email=request.POST["email"]
        password=request.POST["password"]
        if User.objects.filter(username=name):
            messages.warning(request,"username is already taken!")
            return redirect("register")    
        if User.objects.filter(email=email):
            messages.warning(request,"email is already taken!")
            return redirect("register")
        else:
            us=User.objects.create_user(username=name,email=email,password=password)
            us.is_staff=True
            us.save()
            
            reg=employee(user=us,employee_id=empid,employee_email=email)
            reg.save()
            
            messages.success(request,'Your account has been created! You are able to login')
            return redirect("/signin")
    return render(request,"signup.html")

def user_login(request):
    if request.method=="POST":
        un = request.POST["username"]
        empid=request.POST["employeeid"]
        pwd = request.POST["password"]
      
        user = authenticate(username=un,password=pwd,empid=empid)
        if user:
            login(request,user)
            if user.is_superuser:
                return HttpResponseRedirect("/admin")
            else:
                res = HttpResponseRedirect("/userhome")
                if "rememberme" in request.POST:
                    res.set_cookie("user_id",user.id)
                    res.set_cookie("date_login",datetime.now())
                return res         
        else:
            messages.warning(request,"invalid creditionals")
            return redirect("/signin")
    return render(request,"signin.html")

@login_required
def userhome(request):
    context = {}
    check = employee.objects.filter(user__id=request.user.id)
    if len(check)>0:
        data = employee.objects.get(user__id=request.user.id)
        context["data"] = data
    return render(request,"userhome.html",context)

@login_required
def Update_details(request):
    context = {}
    check = employee.objects.filter(user__id=request.user.id)
    if len(check)>0:
        data = employee.objects.get(user__id=request.user.id)
        context["data"]=data    
    if request.method=="POST":
        department_name=request.POST.get("departmentname")
        employee_name=request.POST.get("empname")
        employee_id=request.POST.get("empid")
        employee_email=request.POST.get("empemail")
        employee_address=request.POST.get("empaddress")
        employee_doj=request.POST.get("empdoj")
        profile=request.FILES.get("image")
        
        usr = User.objects.get(id=request.user.id)
        usr.email=employee_email
        usr.save()

        data.department_name=department_name
        data.employee_id=employee_id
        data.employee_name=employee_name
        data.employee_email=employee_email
        data.employee_address=employee_address
        data.employee_doj=employee_doj
        data.profile=profile
        data.save()
        messages.success(request,"Updated Successfully")
    return render(request,"addemp.html",context)
@login_required
def new_task(request):
    context = {}
    check = task.objects.filter(id=request.user.id)
    if len(check)>0:
        data = task.objects.get(id=request.user.id)
        context["data"]=data    
    if request.method=="POST":
        file=request.FILES.get("file")   
        data.upload_task=file
        data.save()    
    return render(request,"newtask.html",context)
@login_required
def user_logout(request):
    logout(request)
    res =  HttpResponseRedirect("/")
    res.delete_cookie("user_id")
    res.delete_cookie("date_login")
    return res

def user_admin(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        if username and password=="admin":
            return redirect("/user_adminhome")
        else:
            messages.warning(request,"invalid creditionals")
            return redirect("/adminpage")
    return render(request,'admin.html')

def user_adminhome(request):
    return render(request,"adminhome.html")


def view_employee(request):
    data=employee.objects.all()
    return render(request,"emplist.html",{"data":data})

def assign_task(request,id):  
    data=employee.objects.get(id=id)
    if request.method=="POST":
        id=request.POST.get("id")
        employee_id=request.POST.get("employeeid")
        employee_name=request.POST.get("employeename")
        task_title=request.POST.get("tasktitle")
        task_end_date=request.POST.get("taskenddate")        
        data=task()
        data.id=id
        data.employee_id=employee_id
        data.employee_name=employee_name
        data.task_title=task_title
        data.task_end_date=task_end_date
        data.save()
        messages.success(request,"Task Assigned Successfully")
    return render(request,"assigntask.html",{"data":data})

def task_status(request):
    data=task.objects.all()
    return render(request,"taskstatus.html",{"task":data})

def admin_logout(request):
    logout(request)
    res =  HttpResponseRedirect("/")
    return res
