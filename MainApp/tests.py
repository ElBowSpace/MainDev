import datetime

from django.test import SimpleTestCase, TestCase
from MainApp.models import User, Post


class ViewTests(SimpleTestCase):

    def check_template(self, page, template):
        response = self.client.get(page)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name=template)

    def test_view_home(self):
        self.check_template('/', 'index.html')

    def test_base_html(self):
        self.check_template('/base.html', 'base.html')
        
    def test_user_credential_templates(self):
        self.check_template('/register.html', 'register.html')
        self.check_template('/login.html', 'login.html')
        self.check_template('/logout.html', 'logout.html')
        
    def test_post_templates(self):
        self.check_template('/post_delete.html', 'post_delete.html')
        self.check_template('/post_edit.html', 'post_edit.html')
        self.check_template('/post_detail.html', 'post_detail.html')
        self.check_template('/post_list.html', 'post_list.html')
        self.check_template('/post_new.html', 'post_new.html')
        
    def test_user_templates(self):
        self.check_template('/user_delete.html', 'user_delete.html')
        self.check_template('/user_edit.html', 'user_edit.html')
        self.check_template('/user_detail.html', 'user_detail.html')
        self.check_template('/user_list.html', 'user_list.html')
        self.check_template('/user_new.html', 'user_new.html')


class AppTester(TestCase):

    def setup_user(self, first, last, email, password):
        self.user = User.objects.create(
            first_name=first,
            last_name=last,
            email=email,
            password=password,
            active=True
        )
        return self.user

    def setup_post(self, body, time_stamp, user):
        self.post = Post.objects.create(
            body=body,
            time_stamp=time_stamp,
            user=user
        )
        return self.post

    def test_user_creation(self):
        user = self.setup_user('Tester', 'Botz', 'test@mail.com', 'secret')
        self.assertEqual(f'{user.first_name}', 'Tester')
        self.assertEqual(f'{user.last_name}', 'Botz')
        self.assertEqual(f'{user.email}', 'test@mail.com')
        self.assertEqual(f'{user.password}', 'secret')

    def test_post_creation(self):
        body = 'Lorem Ipsum dolor sit amet, ' \
               'consectetur adipiscing elit, ' \
               'sed do eiusmod tempor incididunt ut ' \
               'labore et dolore magna aliqua.'
        time_stamp = datetime.datetime.now()
        user = self.setup_user('Tester', 'Botz', 'test@mail.com', 'secret')
        post = self.setup_post(body, time_stamp, user)
        self.assertEqual(f'{post.body}', body)
        self.assertEqual(f'{user.id}', '1')
