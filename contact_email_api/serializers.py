import re
from rest_framework import serializers
from contact_email_app.models import Contact
from contact_email_app.tasks import send_email_task


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'text']

    def create(self, validate_data):
        instance = super(ContactSerializer, self).create(validate_data)
        message = 'NAME: {name} / EMAIL: {email}: '.format(
            name=validate_data['name'],
            email=validate_data['email'])
        message += '\n\n{0}'.format(validate_data['text'])
        send_email_task.delay(message=message)
        return instance

    def validate_text(self, value):
        if len(value) > 2000:
            raise serializers.ValidationError('No more than 2000 characters please')
        if len(value) < 15:
            raise serializers.ValidationError('Minimum 15 characters')
        return value

    def validate_name(self, value):
        punct = ['!', '@', '#', '$', '%', '&', '*', '(', ')', '[', ']', '/', '?', '+', '-', '^', ',', '.', '<', '>',
                 '|', '`', '~', ':', ';', '{', '}', '"', '№', '\'', '\\', '€', '£', '¢', '¥', '§', '°', '_']
        for i in value:
            if i in punct:
                raise serializers.ValidationError('Name cannot contains special chars and punctuations.')
        if re.search(r'\d', value):
            raise serializers.ValidationError('The name cannot contains numbers')
        if re.search(r'\s', value):
            raise serializers.ValidationError('The name cannot contains spaces')
        return value
