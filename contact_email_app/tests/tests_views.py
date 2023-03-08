from django.test import TestCase
from django.urls import reverse

from contact_email_app.views import AboutView, HomePage, SuccessView


class TestGetPages(TestCase):
    def test_home_page_get(self):
        check_template = HomePage()
        response = self.client.get(reverse('contact_email_app:home'))

        self.assertEqual(check_template.template_name, 'contact_email_app/home.html')
        self.assertEqual(response.status_code, 200)

    def test_about_page_get(self):
        check_template = AboutView()
        response = self.client.get(reverse('contact_email_app:about'))

        self.assertEqual(check_template.template_name, 'contact_email_app/about.html')
        self.assertEqual(response.status_code, 200)

    def test_success_page_get(self):
        check_template = SuccessView()
        response = self.client.get(reverse('contact_email_app:success'))

        self.assertEqual(check_template.template_name, 'contact_email_app/success.html')
        self.assertEqual(response.status_code, 200)
