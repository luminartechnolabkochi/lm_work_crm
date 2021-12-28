from django.urls import path
from crm import views

urlpatterns=[
    path("departments/add",views.Departments.as_view(),name="department"),
    path("employees/add",views.UserRegistration.as_view(),name="signup"),
    path("",views.SignIn.as_view(),name="signin"),
    path("accounts/signout",views.signout,name="signout"),
    path("employees/all",views.Employees.as_view(),name="employees"),
    path("employee/<int:id>",views.EmployeeDetail.as_view(),name="empdetail")
]