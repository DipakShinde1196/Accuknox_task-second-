# signals.py
from django.dispatch import Signal, receiver
import threading

# Define a custom signal
my_signal = Signal()

# Define a receiver function
@receiver(my_signal)
def my_receiver(sender, **kwargs):
    print(f"Receiver running in thread: {threading.current_thread().name}")
