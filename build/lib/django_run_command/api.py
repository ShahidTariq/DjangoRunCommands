# from django.http import JsonResponse
# import threading
# from django.core import management
#
# from django_run_command.models import ThreadTask
#
# @staticmethod
# def start_thread_task(command, arg=None):
#     task = ThreadTask()
#     task.save()
#     t = threading.Thread(target=long_task,args=[task.id, command, arg])
#     t.setDaemon(True)
#     t.start()
#     return JsonResponse({'id': task.id})
#
# @staticmethod
# def check_thread_task(id):
#     task = ThreadTask.objects.get(pk=id)
#     return JsonResponse({'is_done': task.is_done})
#
# @staticmethod
# def long_task(id, command, arg):
#     if arg:
#         management.call_command(command, arg)
#     else:
#         management.call_command(command, interactive=False)
#     task = ThreadTask.objects.get(pk=id)
#     task.is_done = True
#     task.save()
