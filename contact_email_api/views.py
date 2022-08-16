from rest_framework import generics
from contact_email_app.models import Contact
from contact_email_api.serializers import ContactSerializer


class ContactCreate(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
