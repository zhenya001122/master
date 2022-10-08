from django.contrib import admin
from users.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'age')
    list_filter = ('email', 'first_name', 'last_name', 'age')
    search_fields = ('email', 'first_name', 'last_name')

admin.site.register(User, UserAdmin)