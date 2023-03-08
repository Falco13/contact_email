from django.test import TestCase
from contact_email_app.models import Contact


class TestModelContact(TestCase):
    @classmethod
    def setUpTestData(cls):
        Contact.objects.create(name='Billy',
                               email='billy@test.com',
                               text='My name is Billy. This is test text',
                               is_done=False)

    def test_name_field(self):
        contact = Contact.objects.get(id=1)
        field_label = contact._meta.get_field('name').verbose_name

        self.assertEqual(field_label, 'name')
        self.assertEqual(contact.name, 'Billy')

    def test_email_field(self):
        contact = Contact.objects.get(id=1)
        field_label = contact._meta.get_field('email').verbose_name

        self.assertEqual(field_label, 'email')
        self.assertEqual(contact.email, 'billy@test.com')

    def test_text_field(self):
        contact = Contact.objects.get(id=1)
        field_label = contact._meta.get_field('text').verbose_name

        self.assertEqual(field_label, 'message')
        self.assertEqual(contact.text, 'My name is Billy. This is test text')

    def test_is_done_field(self):
        contact = Contact.objects.get(id=1)
        field_label = contact._meta.get_field('is_done').verbose_name

        self.assertEqual(field_label, 'done')
        self.assertEqual(contact.is_done, False)

    def test_created_at_field(self):
        contact = Contact.objects.get(id=1)
        field_label = contact._meta.get_field('created_at').verbose_name

        self.assertEqual(field_label, 'date of creation')

    def test_updated_at_field(self):
        contact = Contact.objects.get(id=1)
        field_label = contact._meta.get_field('updated_at').verbose_name

        self.assertEqual(field_label, 'update date')

    def test_name_max_length(self):
        contact = Contact.objects.get(id=1)
        max_length = contact._meta.get_field('name').max_length

        self.assertEqual(max_length, 15)

    def test_object_str_(self):
        contact = Contact.objects.get(id=1)
        expected_object_name = f'Name: {contact.name}, Done: {contact.is_done}'

        self.assertEqual(str(contact), expected_object_name)
