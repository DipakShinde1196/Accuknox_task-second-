Question 2: Do Django signals run in the same thread as the caller?

Yes, by default, Django signals run in the same thread as the caller. This means that when a signal is sent, the receiver function executes within the same thread as the signal sender.
