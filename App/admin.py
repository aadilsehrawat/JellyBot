from django.contrib import admin
from .models import *

# Register your models here.
class ActionAdmin(admin.ModelAdmin):
    list_display = ('action', 'description', 'performed')

class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')

class PerformLogsAdmin(admin.ModelAdmin):
    list_display = ('action', 'input_file', 'output_file')

class ActionMediaAdmin(admin.ModelAdmin):
    list_display = ('action', 'media')

admin.site.register(Actions, ActionAdmin)
admin.site.register(ContactUs, ContactUsAdmin)
admin.site.register(PerformLogs, PerformLogsAdmin)
admin.site.register(ActionMedia, ActionMediaAdmin)