from django.contrib import admin
from .models import *

# Register your models here.
class ActionAdmin(admin.ModelAdmin):
    list_display = ('action', 'description', 'times_performed')

class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')

class ActionStepsAdmin(admin.ModelAdmin):
    list_display = ('action',)
# class PerformLogsAdmin(admin.ModelAdmin):
#     list_display = ('action', 'input_file', 'output_file')

admin.site.register(Actions, ActionAdmin)
admin.site.register(ContactUs, ContactUsAdmin)
admin.site.register(ActionSteps, ActionStepsAdmin)
# admin.site.register(PerformLogs, PerformLogsAdmin)