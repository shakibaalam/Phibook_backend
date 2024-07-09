from django.contrib import admin
from .models import Post, Like, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'title', 'created_at', 'updated_at')
    list_filter = ('author', 'created_at',)
    search_fields = ('title', 'content',)
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'post', 'created_at')
    list_filter = ('user', 'post',)
    search_fields = ('user__username', 'post__title',)
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'post', 'content', 'created_at', 'updated_at')
    list_filter = ('user', 'post', 'created_at',)
    search_fields = ('user__username', 'post__title', 'content',)
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)

