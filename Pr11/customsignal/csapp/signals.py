from django.dispatch import Signal, receiver


# create our custom signal

notification = Signal()
notification.providing_args = ['request', 'user']
# receiver function


@receiver(notification)
def show_notification_signal(sender, **kwargs):
    print(sender)
    print(f'{kwargs}')
    print("hey it is notification signal----------------")
