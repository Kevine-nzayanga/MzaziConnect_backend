from django.contrib import admin
from .models import Comment

class CommentAdmin(admin.ModelAdmin):
        list_display = ('assignment','commentor', 'content', 'created_at', 'updated_at')


admin.site.register(Comment, CommentAdmin)


# Register your models here.
