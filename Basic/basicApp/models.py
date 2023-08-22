from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=255, null=True)
    description = models.TextField(blank=True, null=True)
    author = models.CharField(max_length=255, null=True)
    publication = models.CharField(max_length=255, null=True)
