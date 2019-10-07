from django.contrib import admin
from .models import Users,UserProfile

# Register your models here
admin.site.register(Users)
admin.site.register(UserProfile)