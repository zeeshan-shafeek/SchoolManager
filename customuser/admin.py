from django.contrib import admin
from .models import CustomUser



class CustomUserAdmin(admin.ModelAdmin):    
    list_display = ('username', 'email', 'first_name')
    list_filter = ('is_staff', 'is_superuser')
    fields = (
        'email',
        'username',
        'password',
        'first_name',
        'last_name',
        'account_type',

    )


    
    

admin.site.register(CustomUser, CustomUserAdmin)


# Register your models here.
