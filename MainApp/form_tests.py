import datetime
from MainApp.models import User, Post
from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse

from .forms import *
from .post import *
from .user import *


# Old man McEwen's forms tester
class TestForm(SimpleTestCase):
    # python manage.py test MainApp.form_tests.TestForm
    # python manage.py test MainApp.form_tests.TestForm.test_registration_form

    # ----------------------------------------------------------------
    # User Forms Tests
    def test_registration_form(self):
        form = RegisterForm(data={
            'first_name': 'Test',
            'last_name': 'Dummy',
            'email': 'faux@email.com',
            'password': 'theDuckKnows'
        })

        self.assertTrue(form.is_valid())

    def test_registration_form_blank(self):
        form = RegisterForm(data={})
        # self.assertTrue(form.is_valid())
        self.assertEqual(len(form.errors), 4)

    def test_login_form(self):
        form = LoginForm(data={
            'email': 'faux@email.com',
            'password': 'theDuckKnows'
        })

        self.assertTrue(form.is_valid())

    def test_login_form_blank(self):
        form = LoginForm(data={})
        # self.assertTrue(form.is_valid())
        self.assertEqual(len(form.errors), 2)

    def test_edit_user_form(self):
        form = EditUserForm(data={
            'first_name': 'Test',
            'last_name': 'Dummy',
            'email': 'faux@email.com',
            'password': 'theDuckKnows'
        })

        self.assertTrue(form.is_valid())

    def test_edit_user_form_blank(self):
        form = EditUserForm(data={})
        # self.assertTrue(form.is_valid())
        self.assertEqual(len(form.errors), 4)

    # ----------------------------------------------------------------
    # Post Forms

    def test_new_post_form(self):
        form = NewPostForm(data={
            'body': 'Have you ever seen the seagulls as '
                    'they fly amongst the heavens',

        })

        self.assertTrue(form.is_valid())

    def test_new_post_form_blank(self):
        form = NewPostForm(data={})
        # self.assertTrue(form.is_valid())
        self.assertEqual(len(form.errors), 1)

    def test_edit_post_form(self):
        form = EditPostForm(data={
            'body': 'Have you ever seen the seagulls as '
                    'they fly amongst the heavens',

        })

        self.assertTrue(form.is_valid())

    def test_edit_post_form_blank(self):
        form = EditPostForm(data={})
        # self.assertTrue(form.is_valid())
        self.assertEqual(len(form.errors), 1)
