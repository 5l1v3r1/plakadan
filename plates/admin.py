from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from plates.models import User, Plate


class ExtendedUserAdmin(UserAdmin):
    model = User

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone_number',)}),
    )


class PlateAdmin(admin.ModelAdmin):
    model = Plate
    list_display = ('plate', 'owner')


admin.site.register(User, ExtendedUserAdmin)
admin.site.register(Plate, PlateAdmin)
