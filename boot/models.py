from email import message
from operator import truediv
from django.db import models

# Create your models here.

class Inquiry(models.Model):
    fullname  = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    phone_number = models.IntegerField()
    inquiry_message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self) -> str:
    #     return f"{self.id}.{self.title}"
