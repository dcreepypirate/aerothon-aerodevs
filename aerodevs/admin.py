from django.contrib import admin

# Register your models here.
from .models import User
from .models import Product,Order

class OrderAdmin(admin.ModelAdmin):
    order_display = ["buyer","part"]

class UserAdmin(admin.ModelAdmin):
    user_display = ["username","password","email","role"]

admin.site.register(User, UserAdmin)
admin.site.register(Product)
admin.site.register(Order, OrderAdmin)


