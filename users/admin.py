from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Branch, Customer, Employee

# Register your models here.


class BranchAdmin(admin.ModelAdmin):
    list_display = [
        'district',
        'address',
        'photo',
    ]
    search_fields = [
        'district',
    ]
    list_filter = [
        'district',
    ]


class CustomerInline(admin.StackedInline):
    model = Customer
    can_delete = False


class CustomerAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'phone_number',
        'profile_photo',
    ]
    search_fields = [
        'phone_number',
    ]
    list_filter = [
        'phone_number',
    ]
    list_display_links = [
        'user',
        'phone_number',
    ]


class EmployeeInline(admin.StackedInline):

    model = Employee
    can_delete = False
    
class EmployeeAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'phone_number',
        'profile_photo',
        'services_done',
        'work_at',
    ]
    search_fields = [
        'user',
    ]
    list_filter = [
        'user',
    ]
    readonly_fields = [
        'services_done',
    ]
    list_editable = [
        'work_at',
    ]
    list_display_links = [
        'user',
        'phone_number',
    ]

class UserAdmin(BaseUserAdmin):
    inlines = [CustomerInline, EmployeeInline]

#Branch model
admin.site.register(Branch, BranchAdmin)

#Employee model
admin.site.register(Customer, CustomerAdmin)

#Customer model
admin.site.register(Employee, EmployeeAdmin)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
