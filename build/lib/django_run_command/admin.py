from django.contrib import admin

from .models import ManagementCommand


class ManagementCommandAdmin(admin.ModelAdmin):
    list_display = ['command', 'args', 'created_on', 'status', 'output']

    def get_form(self, request, obj=None, **kwargs):
        self.exclude = ['created_on', 'status', 'output']
        return super(ManagementCommandAdmin, self).get_form(request, obj, **kwargs)


admin.site.register(ManagementCommand, ManagementCommandAdmin)
