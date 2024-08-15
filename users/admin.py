from django.contrib import admin
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


admin.site.register(Branch, BranchAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Employee, EmployeeAdmin)
