from django.contrib import admin

# Register your models here.
from .models import User



class UserAdmin(admin.ModelAdmin):
    user_display = ["username","password","email","role"]

admin.site.register(User, UserAdmin)

