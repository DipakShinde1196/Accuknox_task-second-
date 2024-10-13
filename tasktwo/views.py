import threading
from django.http import HttpResponse
from .signals import my_signal

def trigger_signal(request):
    print(f"Signal sender running in thread: {threading.current_thread().name}")
    my_signal.send(sender=None)
    return HttpResponse("Signal sent")
