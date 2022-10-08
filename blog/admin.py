from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'text', 'created_at')
    list_filter = ('author',)
    search_fields = ('author', 'title', 'text', 'created_at')