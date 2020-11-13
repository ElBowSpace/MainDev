from .models import User


def add_user(first_name, last_name, email, password):
    u = User.objects.create(first_name=first_name,
                            last_name=last_name,
                            email=email,
                            password=password,
                            is_active=True
                            )
    u.save()
    return u


def edit_user(old_first, old_last, new_first=None,
              new_last=None, new_email=None, new_password=None):
    user = User.objects.get(first_name=old_first, last_name=old_last)
    if new_first is not None:
        user.first_name = new_first
    if new_last is not None:
        user.last_name = new_last
    if new_email is not None:
        user.email = new_email
    if new_password is not None:
        user.password = new_password
    user.save()


def get_user(first_name, last_name):
    return User.objects.get(first_name=first_name, last_name=last_name)


def get_all_users():
    return User.objects.all()


def delete_user(first_name, last_name):
    return User.objects.get(first_name=first_name, last_name=last_name).delete()
