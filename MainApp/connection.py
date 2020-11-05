from .models import Connection


def make_connection(sender, receiver):
    new_connection = Connection.objects.create(sender=sender,
                                               receiver=receiver,
                                               active=True)
    new_connection.save()
    return new_connection