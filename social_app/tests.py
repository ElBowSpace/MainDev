from django.contrib.auth.models import User
from django.test import SimpleTestCase, TestCase
from social_app.user import add_user, get_user


# -----------------------------------------------------
#   S I M P L E - - V I E W S
#
class SimpleViewTests(SimpleTestCase):
    # python manage.py test social_app.tests.SimpleViewTests
    # python manage.py test social_app.tests.SimpleViewTests.test_view_index
    def check_template(self, page, template):
        print()
        print("simple view test: " + template)
        response = self.client.get(page)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name=template)
        print("test view validated")

    def test_view_index(self):
        self.check_template('/', 'index.html')

    def test_view_tutorial(self):
        self.check_template('/user_guide/', 'tutorial.html')

    def test_view_signup(self):
        self.check_template('/accounts/signup/', 'registration/signup.html')

    def test_view_login(self):
        self.check_template('/accounts/login/', 'registration/login.html')

    def test_view_user_list(self):
        self.check_template('/users/', 'user_list.html')

    def test_view_post_list(self):
        self.check_template('/posts/', 'post_list.html')

    def test_view_missing(self):
        self.check_template('/missing/', '_missing.html')


# -----------------------------------------------------
#   U S E R - - C R U D
#
class UserCRUD(TestCase):
    # python manage.py test social_app.tests.UserCRUD
    # python manage.py test social_app.tests.UserCRUD.test_user_creation
    def setup_user(self, username, first, last, email, password):
        self.user = User.objects.create(
            username=username,
            first_name=first,
            last_name=last,
            email=email,
            password=password,
        )
        return self.user

    def test_user_creation(self):
        user = self.setup_user('named', 'Tester', 'Bot', 'bot@fake.com', 'secret')
        self.assertEqual(f'{user.username}', 'named')
        self.assertEqual(f'{user.first_name}', 'Tester')
        self.assertEqual(f'{user.last_name}', 'Bot')
        self.assertEqual(f'{user.email}', 'bot@fake.com')
        self.assertEqual(f'{user.password}', 'secret')

    def test_user_update(self):
        user = self.setup_user('tester', 'first', 'last', 'email@address.net', 'password')
        self.assertEqual(f'{user.email}', 'email@address.net')
        user.email = 'newer@address.net'
        self.assertEqual(f'{user.email}', 'newer@address.net')

    def test_add_new_user(self):
        username = 'testuser'
        useradd = add_user(username, 'Atomic', 'User', 'aTomic@users.com', 'hidden')
        self.assertEqual(get_user(username).first_name, useradd.first_name)

    def test_uniqueness_of_username(self):
        # this required some finagling in user dot py to test as the
        # Auth_User model blocks duplicates implicitly
        username = 'testusers'
        useradd1 = add_user(username, 'Atomic', 'User', 'aTomic@users.com', 'hidden')
        useradd2 = add_user(username, 'Binary', 'User', 'aTomiK@users.com', 'secret')
        self.assertEqual(get_user(username).first_name, useradd1.first_name)
        self.assertEqual(None, useradd2)

# TODO User crud delete and edit
# TODO Post crud

# import datetime
#
# from django.test import TestCase, Client
# from django.urls import reverse
# from social_app.models import User, Post
# from .user import *
# from .post import *
# from .connection import *
# # python manage.py test
# # -----------------------------------------------------
# #   N O N C R U D
# class AppTester(TestCase):
#     # python manage.py test social_app.tests.AppTester
#     # python manage.py test social_app.tests.AppTester.test_user_creation
#     def setup_post(self, body, time_stamp, user):
#         self.post = Post.objects.create(
#             body=body,
#             time_stamp=time_stamp,
#             user=user
#         )
#         return self.post
#

#
#     def test_post_creation(self):
#         body = 'Lorem Ipsum dolor sit amet, ' \
#                'consectetur adipiscing elit, ' \
#                'sed do eiusmod tempor incididunt ut ' \
#                'labore et dolore magna aliqua.'
#         time_stamp = datetime.datetime.now()
#         user = self.setup_user('userillamo', 'Tester', 'Botz', 'test@mail.com', 'secret')
#         post = self.setup_post(body, time_stamp, user)
#         self.assertEqual(f'{post.body}', body)
#         self.assertEqual(f'{user.id}', '1')
#
#     def check_template(self, page, template):
#         response = self.client.get(page)
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, template_name=template)
#
#     def test_post_templates(self):
#         #     self.check_template('/post_delete.html', 'post_delete.html')
#         #     self.check_template('/post_edit.html', 'post_edit.html')
#         #     self.check_template('/post_detail.html', 'post_detail.html')
#         self.check_template('/posts/', 'post_list.html')
#
#
#     def test_user_templates(self):
#         #     self.check_template('/user_delete.html', 'user_delete.html')
#         #     self.check_template('/user_edit.html', 'user_edit.html')
#         #     self.check_template('/user/', 'user_detail.html')
#         self.check_template('/users/', 'user_list.html')
#
#
# # -----------------------------------------------------
# #   U S E R C R U D
# #
# class UserCRUDTest(TestCase):
#     # python manage.py test social_app.tests.UserCRUDTest
#     # python manage.py test social_app.tests.UserCRUDTest.test_a_new_user
#
#     def test_c_get_user(self):
#         username = 'uname'
#         first = 'fname'
#         last = 'lname'
#         add_user(username, first, last, 'test@mail.com', 'secret')
#         u = get_user(first_name=first, last_name=last)
#         self.assertEqual(u.first_name, first)
#         self.assertEqual(u.last_name, last)
#
#     def test_d_get_all(self):
#         add_user('Jsmith', "John", "Smith", 'test@mail.com', 'secret')
#         add_user('Ksmith', "Karen", "Smith", 'test@mail.com', 'secret')
#         add_user('Josmith', "Jordan", "Smith", 'test@mail.com', 'secret')
#         print(get_all_users())
#
#     def test_e_delete(self):
#         add_user("JohSmith", "John", "Smith", 'test@mail.com', 'secret')
#         add_user("KaSmith", "Karen", "Smith", 'test@mail.com', 'secret')
#         add_user("JorSmith", "Jordan", "Smith", 'test@mail.com', 'secret')
#         delete_user("Karen", "Smith")
#         print(get_all_users())
#
#
# # -----------------------------------------------------
# #   P O S T C R U D
# #
# class PostCRUDTest(TestCase):
#     # python manage.py test social_app.tests.PostCRUDTest
#     # python manage.py test social_app.tests.PostCRUDTest.test_a_new_post
#
#     def create_and_get_user(self):
#         return add_user('user_name', 'first_name', 'last_name', 'test@mail.com', 'secret')
#
#     def generic_post_body_a(self):
#         return 'Lorem Ipsum dolor sit amet, ' \
#                'consectetur adipiscing elit, ' \
#                'sed do eiusmod tempor incididunt ut ' \
#                'labore et dolore magna aliqua.'
#
#     def generic_post_body_b(self):
#         return 'Neque porro quisquam est, ' \
#                'qui dolorem ipsum quia dolor ' \
#                'sit amet, consectetur, adipisci velit, ' \
#                'sed quia non numquam eius modi tempora ' \
#                'incidunt ut labore et dolore magnam aliquam ' \
#                'quaerat voluptatem.'
#
#     def test_a_new_post(self):
#         body = 'Lorem Ipsum dolor sit amet, ' \
#                'consectetur adipiscing elit, ' \
#                'sed do eiusmod tempor incididunt ut ' \
#                'labore et dolore magna aliqua.'
#         time_stamp = datetime.datetime.now()
#         uname = 'username'
#         first = 'fname'
#         last = 'lname'
#         user = add_user(uname, first, last, 'test@mail.com', 'secret')
#         post = add_post(body, time_stamp, user)
#         self.assertEqual(post.body, body)
#         self.assertTrue(type(post.id) is int)
#
#     def test_b_edit_post(self):
#         user = self.create_and_get_user()
#         time_stamp = datetime.datetime.now()
#         body = self.generic_post_body_a()
#         post = add_post(body, time_stamp, user)
#         new_body = self.generic_post_body_b()
#         edit_post(post.id, new_body)
#         post = Post.objects.get(id=post.id)
#         self.assertEqual(post.body, new_body)
#
#     def test_c_get_post(self):
#         user = self.create_and_get_user()
#         time_stamp = datetime.datetime.now()
#         body = self.generic_post_body_b()
#         post = add_post(body, time_stamp, user)
#         self.assertEqual(post.body, get_post(post.id).body)
#
#     def test_d_get_all_posts(self):
#         user = self.create_and_get_user()
#         time_stamp = datetime.datetime.now()
#         body = self.generic_post_body_b()
#         add_post(body, time_stamp, user)
#
#         self.assertEqual(get_all_posts().count(), 1)
#
#         time_stamp = datetime.datetime.now()
#         body = self.generic_post_body_a()
#         add_post(body, time_stamp, user)
#
#         self.assertEqual(get_all_posts().count(), 2)
#
#         time_stamp = datetime.datetime.now()
#         body = self.generic_post_body_b()
#         add_post(body, time_stamp, user)
#
#         self.assertEqual(get_all_posts().count(), 3)
#
#     def test_e_delete_post(self):
#         user = self.create_and_get_user()
#         time_stamp = datetime.datetime.now()
#         body = self.generic_post_body_a()
#         post = add_post(body, time_stamp, user)
#         self.assertEqual(get_all_posts().count(), 1)
#         delete_post(post.id)
#         self.assertEqual(get_all_posts().count(), 0)
#
#
# # -----------------------------------------------------
# #   U S E R C R E A T I O N
# #
# # class UserCreationTest(TestCase):
# #     # python manage.py test social_app.tests.UserCreationTest
# #     # python manage.py test social_app.tests.UserCreationTest.test_a_description
# #
# #     def test_a_new_user_redirect(self):
# #         # c = Client()
# #         response = self.client.post('user/new/', data={'first_name': 'test', 'last_name': 'user',
# #                                             'email': 'test@user.com', 'password': 'simplepass'})
# #         self.assertContains(response, 'first_name')
#
# # -----------------------------------------------------
# class ConnectionCRUDTests(TestCase):
#
#     def user_setup(self, username, first, last, email, password):
#         self.user = User.objects.create(
#             username=username,
#             first_name=first,
#             last_name=last,
#             email=email,
#             password=password,
#             is_active=True
#         )
#         return self.user
#
#     def test_connection(self):
#         u1 = self.user_setup('primero', 'first', 'butnotlast', '70sneverdied@yahoo.com', 'haha4378')
#         u2 = self.user_setup('deus', 'dos', 'anddeflast', 'trumpfailed@yahoo.com', 'partytime89')
#         connect_users(u1, u2)
#         check_connection(u1, u2)
#         self.assertEqual(check_connection(u1, u2), True)
#         self.assertEqual(check_connection(u2, u1), True)
#
#     def test_multiple_connections(self):
#         u1 = self.user_setup('primero', 'first', 'butnotlast', '70sneverdied@yahoo.com', 'haha4378')
#         u2 = self.user_setup('deus', 'dos', 'anddeflast', 'trumpfailed@yahoo.com', 'partytime89')
#         u3 = self.user_setup('tres', 'first', 'butnotlast', 'dontcare1@aol.com', 'haha4378')
#         u4 = self.user_setup('quatro', 'dos', 'anddeflast', 'dontcare2@aol.com', 'partytime89')
#         u5 = self.user_setup('cinco', 'first', 'butnotlast', 'dontcare3@aol.com', 'haha4378')
#         u6 = self.user_setup('seis', 'dos', 'anddeflast', 'dontcare4@aol.com', 'partytime89')
#         connect_users(u1, u2)
#         connect_users(u2, u4)
#         self.assertEqual(check_connection(u1, u2), True)
#         self.assertEqual(check_connection(u1, u3), False)
#         self.assertEqual(check_connection(u2, u3), False)
