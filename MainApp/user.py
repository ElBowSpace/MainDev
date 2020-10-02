from .models import User


def add_user(first_name, last_name, email, password):
    return User.objects.create(first_name=first_name,
                               last_name=last_name,
                               email=email,
                               password=password,
                               active=True
                               )


def edit_user():
    pass


def get_user():
    pass


def get_all_users():
    pass


def delete_user():
    pass
