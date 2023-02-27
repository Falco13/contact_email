from django.urls import reverse_lazy
from django.views import generic
from contact_email_app.forms import ContactForm
from contact_email_app.tasks import send_email_task


class HomePage(generic.CreateView, generic.FormView):
    form_class = ContactForm
    template_name = 'contact_email_app/home.html'
    success_url = reverse_lazy('contact_email_app:success')

    def form_valid(self, form):
        message = 'NAME: {name} / EMAIL: {email}: '.format(
            name=form.cleaned_data.get('name'),
            email=form.cleaned_data.get('email'))
        message += '\n\n{0}'.format(form.cleaned_data.get('text'))
        send_email_task.delay(message=message)
        return super(HomePage, self).form_valid(form)


class AboutView(generic.TemplateView):
    template_name = 'contact_email_app/about.html'


class SuccessView(generic.TemplateView):
    template_name = 'contact_email_app/success.html'
