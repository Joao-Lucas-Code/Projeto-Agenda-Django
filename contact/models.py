from django.db import models
from django.utils import timezone
# Create your models here.

class Contact(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)