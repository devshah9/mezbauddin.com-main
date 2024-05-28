from django.db import models

class Menu(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    # Add any other fields you need