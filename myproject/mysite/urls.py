from django.urls import path
from mysite import views
urlpatterns = [
    path("",views.home,name="home"),
    path("signup/",views.register,name="register"),
    path('signin/',views.user_login,name="user_login"),
    path("userhome/",views.userhome,name="userhome"),
    path("addemp/",views.employee,name="addemp"),
    path("user_logout/",views.user_logout,name="user_logout"),
    path("user_admin/",views.user_admin,name="user_admin"),
    path("user_adminhome/",views.user_adminhome,name="user_adminhome"),
    path("update_details/",views.Update_details,name="update_details"),
    path("view_employee/",views.view_employee,name="view_employee"),
    path("assign_task/<int:id>",views.assign_task,name="assign_task"),
    path("task_status/",views.task_status,name="task_status"),
    path("new_task/",views.new_task,name="new_task"),
    path("admin_logout/",views.admin_logout,name="admin_logout"),
    
]
