from django.contrib import admin
from . models import users

class UsersAdmin(admin.ModelAdmin):
    list_display = ('username', 'role', 'cidade')
    search_fields = ('username', 'role', 'cidade')
    filter_horizontal = ('groups', 'user_permissions')

admin.site.register(users)
