from django.conf import settings
from django.db import models
from django.core import management
from django.db.models import signals


class ManagementCommand(models.Model):
    """ Run management commands from admin """
    command = models.CharField(max_length=500, help_text="Select management command",
                                       choices=settings.COMMAND_CHOICES, null=True, blank=True)

    args = models.CharField(max_length=1000, blank=True, null=True, help_text="Enter argument separated by ;")
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
        args = instance.args
        options = None
        if args:
            options = set(str(args).split(';'))
        try:
            if options:
                management.call_command(command, *options)
            else:
                management.call_command(command)
            output = command + " done successfully"
            status = True
        except Exception as ex:
            output = 'Error running management command, see {}'.format(str(ex))
            status = False
        ManagementCommand.objects.filter(id=instance.id).update(output=output, status=status)

signals.post_save.connect(ManagementCommand.execute, sender=ManagementCommand)
