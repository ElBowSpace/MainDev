from .models import User


def add_user(username, first_name, last_name, email, password):
    if username is not None:
        if get_user(username) is None:
            user = User.objects.create(username=username,
                                       first_name=first_name,
                                       last_name=last_name,
                                       email=email,
                                       password=password
                                       )
            user.save()
            return user
    else:
        return None


def edit_user(username=None, new_first=None,
              new_last=None, new_email=None, new_password=None):
    if username is not None:
        user = get_user(username=username)
        if new_first is not None:
            user.first_name = new_first
        if new_last is not None:
            user.last_name = new_last
        if new_email is not None:
            user.email = new_email
        if new_password is not None:
            user.password = new_password
        user.save()
        return user
    else:
        return None


def get_user(username=None):
    if username is not None:
        try:
            user = User.objects.get(username=username)
            return user
        except User.DoesNotExist:
            return None
    else:
        return None


def get_all_users():
    return User.objects.all()


def delete_user(username=None):
    if username is not None:
        return User.objects.get(username=username).delete()
    else:
        return False
