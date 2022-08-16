from django.urls import path
from contact_email_api.views import ContactCreate

urlpatterns = [
    path('', ContactCreate.as_view()),
]
