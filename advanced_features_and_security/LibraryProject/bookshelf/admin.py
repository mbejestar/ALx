from django.contrib import admin  
from .models import CustomUser  
from django.contrib.auth.admin import UserAdmin  

class CustomUserAdmin(UserAdmin):  
    model = CustomUser  
    fieldsets = UserAdmin.fieldsets + (  
        (None, {'fields': ('date_of_birth', 'profile_photo')}),  
    )  
    add_fieldsets = UserAdmin.add_fieldsets + (  
        (None, {'fields': ('date_of_birth', 'profile_photo')}),  
    )  

admin.site.register(CustomUser, CustomUserAdmin)
