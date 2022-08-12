from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import get_user_model
# Register your models here.
# class UserAdmin(BaseUserAdmin):
    # list_display = ('email', 'username', 'is_admin')

CustomUser = get_user_model()
class UserAdmin(BaseUserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ('email', 'username', 'is_superuser')

admin.site.register(CustomUser, UserAdmin)

