from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=15)
    email = models.EmailField()
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return f'Name: {self.name}, Done: {self.is_done}'

    class Meta:
        ordering = ['-created_at']
