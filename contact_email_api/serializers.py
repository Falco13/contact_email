from django.conf import settings
from rest_framework import serializers
from contact_email_app.models import Contact
from django.core.mail import send_mail


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'text']

    def create(self, validate_data):
        instance = super(ContactSerializer, self).create(validate_data)
        send_mail(
            subject='THEME: Message {} has been created'.format(instance.pk),
            message='MESSAGE: {}'.format(validate_data),
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.LIST_OF_EMAIL_RECIPIENTS],
            fail_silently=False,
        )
        return instance
