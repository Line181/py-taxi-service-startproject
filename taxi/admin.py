from django.contrib import admin

from taxi.models import Car, Driver, Manufacturer


# Register your models here.

class DriverAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'license_number')

    fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name')
        }),
        ('Additional info', {
            'fields': ('license_number',)
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'license_number'),
        }),
        ('Additional info', {
            'fields': ('license_number',),
        }),
    )


class CarAdmin(admin.ModelAdmin):
    search_fields = ['model']

    list_filter = ['manufacturer']


admin.site.register(Driver, DriverAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(Manufacturer)
