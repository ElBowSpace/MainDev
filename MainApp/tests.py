from django.test import SimpleTestCase
from django.test import TestCase
from django.contrib.auth import get_user_model


# class ViewTests(SimpleTestCase):
#
#     def check_template(self, page, template):
#         response = self.client.get(page)
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, template_name=template)
#
#     def test_view(self):
#         self.check_template('/', 'index.html')
#
#     def test_view_prototype(self):
#         self.check_template('/register.html', 'register.html')
#         self.check_template('/login.html', 'login.html')
#         self.check_template('/post_delete.html', 'post_delete.html')
#         self.check_template('/post_detail.html', 'post_detail.html')
#         self.check_template('/post_edit.html', 'post_edit.html')
#         self.check_template('/base.html', 'base.html')
#         self.check_template('/logout.html', 'logout.html')
#         self.check_template('/post_list.html', 'post_list.html')
#         self.check_template('/post_new.html', 'post_new.html')

class AppTester(TestCase):

    def setup_for_testing(self):
        pass
