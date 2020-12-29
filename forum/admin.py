from django.contrib import admin
from .models import Category, Post, Reply, Rule, ReplyToReply

# Register your models here.

admin.site.register(Category)

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ['created']
    search_fields = ['title','author','content']
    list_filter = ['is_flagged']

admin.site.register(Post, PostAdmin)

class ReplyAdmin(admin.ModelAdmin):
    readonly_fields = ['created']
    search_fields = ['author','content']
    list_filter = ['is_flagged']


admin.site.register(Reply, ReplyAdmin)


class ReplyToReplyAdmin(admin.ModelAdmin):
    readonly_fields = ['created']
    search_fields = ['author','content']
    list_filter = ['is_flagged']


admin.site.register(ReplyToReply)

admin.site.register(Rule)