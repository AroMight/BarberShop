from django.contrib import admin
from .models import Service, Reservation


class JobsInline(admin.StackedInline):
    model = Service.barbers.through


class ReservationAdmin(admin.ModelAdmin):
    list_display = [
        'customer',
        'barber',
        'service',
        'date',
        'time',
        'status',
        'created_at',
    ]
    search_fields = [
        'customer',
        'service',
    ]
    list_filter = [
        'customer',
        'service',
    ]
    list_editable = [
        'status',
        'barber',
    ]
    list_display_links = [
        'customer',
        'service',
        'date',
        'time',
        'created_at',
    ]

class ServiceAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'cover',
        'price',
        # 'duration_time',
        'status',
        'updated_at',
        'is_highlighted',
    ]
    list_editable = [
        'price',
        # 'duration_time',
        'status',
        'is_highlighted',
    ]
    search_fields = [
        'name',
    ]
    list_filter = [
        'name',
    ]
    inlines = [
        JobsInline,
    ]


admin.site.register(Service, ServiceAdmin)
admin.site.register(Reservation, ReservationAdmin)
