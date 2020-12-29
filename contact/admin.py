from django.contrib import admin

from .models import Message
# Register your models here.

class MessageAdmin(admin.ModelAdmin):

    readonly_fields = [
        'remitent',
        'subject',
        'message',
        'img',
        'created',
    ]
    date_hierarchy = ('created')
    search_fields = [
        'remitent',
        'subject',
        'message',
    ]
    list_filter = ['answered']
    list_per_page = 30


admin.site.register(Message,MessageAdmin)
