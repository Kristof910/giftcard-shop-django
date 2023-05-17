from django.db import models


class ContactMessage(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return f"FROM: {self.name}, MESSAGE: {self.message}"
