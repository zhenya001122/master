from django.contrib import admin
from comments.models import Comment, CommentNews


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'product', 'user')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('user', 'text')


@admin.register(CommentNews)
class CommentNewsAdmin(admin.ModelAdmin):
    list_display = ('text', 'news', 'user')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('user', 'text')
