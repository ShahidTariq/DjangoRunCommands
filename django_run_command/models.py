from django.conf import settings
from django.db import models
from django.core import management
from django.db.models import signals


class ManagementCommand(models.Model):
    """ Run management commands from admin """
    command = models.CharField(max_length=100, help_text="Select management command",
                                       choices=settings.COMMAND_CHOICES, null=True, blank=True)

    arg = models.CharField(max_length=100, blank=True, null=True, help_text="Enter argument if any")
    status = models.BooleanField(editable=False, default=False)
    output = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Run Management Command'

    def __str__(self):
        return self.command

    @staticmethod
    def execute(instance, **kwargs):
        command = instance.command
        arg = instance.arg
        try:
            if arg:
                management.call_command(command, arg)
            else:
                management.call_command(command, interactive=False)
            output = command + " done successfully"
            status = True
        except Exception as ex:
            output = 'Error running management command, see {}'.format(str(ex))
        status = False
        ManagementCommand.objects.filter(id=instance.id).update(output=output, status=status)

signals.post_save.connect(ManagementCommand.execute, sender=ManagementCommand)
