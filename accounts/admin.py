from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . models import CustomUser
from . forms import CustomUserCreation, CustomUserChange


@admin.register(CustomUser)
class ModelNameAdmin(UserAdmin):
    add_form = CustomUserCreation
    form = CustomUserChange
    fieldsets = (
        (None, {"fields": ("email", "password", "profile_picture", 'first_name', 'last_name')}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "username", "email", "first_name", "last_name", "password1", "password2", "profile_picture", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
         ),
    )
    list_display = ['username', 'email', "first_name", "last_name"]
    ordering = ('username',)
