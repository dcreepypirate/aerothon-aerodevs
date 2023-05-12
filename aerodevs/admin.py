from django.contrib import admin

# Register your models here.
from .models import User
from .models import Product



class UserAdmin(admin.ModelAdmin):
    user_display = ["username","password","email","role"]

admin.site.register(User, UserAdmin)
admin.site.register(Product)

