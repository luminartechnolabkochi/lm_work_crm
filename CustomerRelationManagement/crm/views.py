from django.shortcuts import render,redirect
from .forms import DepartmentForm,MyUserCreationForm,LoginForm
from django.urls import reverse_lazy
# Create your views here.
from crm.models import *
from django.views.generic import CreateView,TemplateView,ListView,DetailView

from django.contrib.auth import authenticate,login,logout



class Departments(CreateView):
    template_name = "add_dept.html"
    form_class = DepartmentForm
    model = Department
    success_url = reverse_lazy("department")


    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["departments"]=self.model.objects.all()
        return context

class UserRegistration(CreateView):
    model=MyUser
    form_class = MyUserCreationForm
    template_name = "register.html"
    success_url = reverse_lazy("department")

class SignIn(TemplateView):
    template_name = "signin.html"
    form_class=LoginForm
    model=MyUser
    context={}

    def get(self, request, *args, **kwargs):
        form=self.form_class()
        self.context["form"]=form
        return render(request,"signin.html",self.context)
    def post(self,request):
        form=self.form_class(request.POST)
        if form.is_valid():
            email=form.cleaned_data["email"]
            password=form.cleaned_data["password"]
            user=authenticate(request,username=email,password=password)
            if user:
                login(request,user)
                return render(request,"home.html")
            else:
                self.context["form"]=form
                return render(request, "signin.html", self.context)
        else:
            self.context["form"] = form
            return render(request, "signin.html", self.context)

def signout(requset):
    logout(requset)
    return redirect("signin")


class Employees(ListView):
    template_name = "employees.html"
    model=MyUser
    context_object_name = "employees"

class EmployeeDetail(DetailView):
    template_name = "emp_detail.html"
    model=MyUser
    context_object_name = "employee"
    pk_url_kwarg = "id"

