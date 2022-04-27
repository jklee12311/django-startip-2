from operator import truediv
from django.db import models

# Create your models here.

class TempUser(models.Model):
    username = models.CharField(max_length=32)
    email = models.CharField(max_length=32)

class Post(models.Model):
    title  = models.CharField(max_length=32)
    content = models.TextField(blank=True, null=True)
    headimage = models.ImageField(
        upload_to="landing/images/%Y/%m/%d/%H/",
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # likes = models.IntegerField(default=0)
    writer = models.ForeignKey(
        TempUser, 
        on_delete=models.CASCADE,
        blank=True, null=True
        )

    liked_users = models.ManyToManyField(
        TempUser,
        related_name="user_likes" )

    def __str__(self) -> str:
        return f"{self.id}.{self.title}"
