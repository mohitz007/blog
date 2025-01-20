from django.db import models
from django.contrib.auth.models import AbstractUser
import binascii
import os
# Create your models here.

class Author(AbstractUser):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=225, null=True, unique=True)
    password = models.CharField(max_length=128, null=True)



class Token(models.Model):
    user = models.OneToOneField(Author, on_delete=models.CASCADE)
    token = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        if not self.token:
            self.token = self.generate_token()
        super().save(*args, **kwargs)

    def generate_token(self):
        while True:
            token = os.urandom(20).hex()
            if not Token.objects.filter(token=token).exists():
                return token


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.PROTECT)