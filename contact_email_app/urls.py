from django.urls import path
from contact_email_app.views import HomePage, AboutView, SuccessView

app_name = 'contact_email_app'
urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('success/', SuccessView.as_view(), name='success'),
]
