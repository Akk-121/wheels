from django.contrib import admin
from .models import CustomUser,regist,  questions, select, shop, files, buy
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'number', 'email']
    fieldsets = (
        ('Дополнительная информация', {'fields': ('email', 'text')}),
        ('Персональная информация', {'fields': ('first_name', 'last_name', 'number')}),
        ('Права доступа', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Важные даты', {'fields': ('last_login', 'date_joined')})
    )


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(shop)
admin.site.register(select)
admin.site.register(regist)
admin.site.register(questions)
admin.site.register(files)
admin.site.register(buy)
