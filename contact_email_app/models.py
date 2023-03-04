from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=15)
    email = models.EmailField()
    text = models.TextField(verbose_name='message')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='date of creation')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='update date')
    is_done = models.BooleanField(default=False, verbose_name='done')

    def __str__(self):
        return f'Name: {self.name}, Done: {self.is_done}'

    class Meta:
        ordering = ['-created_at']
