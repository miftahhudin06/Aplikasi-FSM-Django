from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from work.forms import KaryawanChangeForm, KaryawanCreateForm

from work.models import BAK, Gedung, Karyawan, Jadwal, Note, TipeGondola

# Register your models here.


class karyawanAdmin(UserAdmin):
    add_form = KaryawanCreateForm
    form = KaryawanChangeForm
    model = Karyawan
    list_display = ("email", "first_name", "last_name",
                    "is_staff", "is_active")
    list_filter = ("email", "is_staff", "is_active",
                   "is_teknisi", "is_admin", "foto")
    fieldsets = (
        (None, {"fields": ("email", "password",
         "first_name", "last_name", "username")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups",
         "user_permissions", "is_teknisi", "is_admin", "foto")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "first_name", "last_name", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions", "is_teknisi", "is_admin", "foto"
            )}
         ),
    )
    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(Karyawan, karyawanAdmin)
admin.site.register(Gedung)
admin.site.register(BAK)
admin.site.register(Note)
admin.site.register(Jadwal)
admin.site.register(TipeGondola)
