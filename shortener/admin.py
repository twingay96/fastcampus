from django.contrib import admin
from .models import Users
from django.contrib.auth.admin import UserAdmin

admin.site.register(Users,UserAdmin)

# Register your models here.
