from .models import Connection


def newname(sender, receiver):
    new_connection = Connection.objects.create(sender=sender,
                                               receiver=receiver,
                                               is_active=True)
    new_connection.save()
    return new_connection