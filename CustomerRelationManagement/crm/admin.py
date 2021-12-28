from django.contrib import admin

# Register your models here.
from crm.models import MyUser,Department
admin.site.register(MyUser)
admin.site.register(Department)

