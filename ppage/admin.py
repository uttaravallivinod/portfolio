from django.contrib import admin
from .models import Messages

# Register your models here.
class MessageAdmin(admin.ModelAdmin):
    list_display = ['email', 'name']


admin.site.register(Messages, MessageAdmin)
