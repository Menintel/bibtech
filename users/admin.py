from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
# Register your models here.


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        ('Role', {'fields': ('is_reader', 'is_lib_staff')}),
    )
    list_display = ('username', 'email', 'is_staff', 'is_reader', 'is_lib_staff')
    list_filter = ('is_staff', 'is_reader', 'is_lib_staff')