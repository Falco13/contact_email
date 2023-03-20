from django.contrib import admin
from contact_email_app.models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'short_text', 'created_at', 'updated_at', 'is_done']
    readonly_fields = ['id', 'name', 'email', 'text', 'created_at', 'updated_at']

    @staticmethod
    def short_text(obj: Contact):
        if len(obj.text) < 150:
            return obj.text
        return obj.text[:150] + '...'
