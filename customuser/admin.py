from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser



class CustomUserAdmin(UserAdmin):    
    list_display = ('username', 'email', 'first_name')
    list_filter = ('is_staff', 'is_superuser')
    
    fieldsets = (
        (None, {'fields': ('username', 'password', 'account_type','is_staff', 'is_superuser',)}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
    
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'account_type', 'is_staff', 'is_superuser'),
        }),

    )
    
    

admin.site.register(CustomUser, CustomUserAdmin)


# Register your models here.
