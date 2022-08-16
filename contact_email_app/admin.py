from django.contrib import admin
from contact_email_app.models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'text', 'created_at', 'updated_at', 'is_done']
    readonly_fields = ['id', 'name', 'email', 'text', 'created_at', 'updated_at']
