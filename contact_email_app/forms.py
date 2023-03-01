import re
from django import forms
from django.core.exceptions import ValidationError
from contact_email_app.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'text']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Your Message'}),
        }

    def clean_text(self):
        text = self.cleaned_data['text']
        if len(text) > 2000:
            raise ValidationError('No more than 2000 characters please')
        if len(text) < 15:
            raise ValidationError('Minimum 15 characters')
        return text

    def clean_name(self):
        name = self.cleaned_data['name']
        punct = ['!', '@', '#', '$', '%', '&', '*', '(', ')', '[', ']', '/', '?', '+', '-', '^', ',', '.', '<', '>',
                 '|', '`', '~', ':', ';', '{', '}']
        for i in name:
            if i in punct:
                raise ValidationError('Name cannot contains special chars and punctuations.')
        if re.match(r'\d', name):
            raise ValidationError('The name cannot start with a number')
        if re.search(r'\d', name):
            raise ValidationError('The name cannot contains numbers')
        if re.search(r'\s', name):
            raise ValidationError('The name cannot contains spaces')
        return name
