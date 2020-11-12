from .models import Connection


def connect_users(sender, receiver):
    new_connection = None
    if not check_connection(sender, receiver):
        new_connection = Connection.objects.create(sender=sender,
                                                   receiver=receiver,
                                                   active=True)
        new_connection.save()
    return new_connection


def check_connection(sender, receiver):
    forward_list = Connection.objects.filter(sender=sender, receiver=receiver)
    reverse_list = Connection.objects.filter(sender=receiver, receiver=sender)
    if len(forward_list) > 0 or len(reverse_list) > 0:
        return True
    else:
        return False
