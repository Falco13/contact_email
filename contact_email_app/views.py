from django.conf import settings
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views import generic
from contact_email_app.forms import ContactForm


class HomePage(generic.CreateView, generic.FormView):
    form_class = ContactForm
    template_name = 'contact_email_app/home.html'
    success_url = reverse_lazy('contact_email_app:success')

    def form_valid(self, form):
        message = "NAME: {name} / EMAIL: {email}: ".format(
            name=form.cleaned_data.get('name'),
            email=form.cleaned_data.get('email'))
        message += "\n\n{0}".format(form.cleaned_data.get('text'))
        send_mail(
            subject='Email from Contact web-site',
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.LIST_OF_EMAIL_RECIPIENTS],
        )
        return super(HomePage, self).form_valid(form)


class AboutView(generic.TemplateView):
    template_name = 'contact_email_app/about.html'


class SuccessView(generic.TemplateView):
    template_name = 'contact_email_app/success.html'
