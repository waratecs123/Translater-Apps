from django.db import models
import random

# Create your models here.
CHOICES = [
    ("/0day/", "/0day/"),
    ("/malware/", "/malware/"),
    ("/opsec/", "/opsec/"),
    ("/carding/", "/carding/"),
    ("/leaks/", "/leaks/"),
    ("/b/", "/b/")
]

class Post(models.Model):
    category = models.CharField(choices=CHOICES, default="/b/", max_length=12, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    nickname = models.CharField(max_length=255, blank=True, default="Anonymus", unique=False)
    text = models.TextField(max_length=5000, blank=False)

    @property
    def id_default(self):
        return random.randint(100000, 999999)

    @property
    def options_default(self):
        return f"{self.text[0:201]}..."

    photo = models.ImageField(null=True, blank=True, upload_to="post/")
    file = models.FileField(null=True, blank=True, upload_to="post/")

    def __str__(self):
        return f"{self.created_at}"


class Comment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    nickname = models.CharField(max_length=255, blank=True, default="Anonymus", unique=False)
    text = models.TextField(max_length=5000, blank=False)

    @property
    def id_default(self):
        return random.randint(100000, 999999)

    @property
    def options_default(self):
        return f"{self.text[0:201]}..."

    photo = models.ImageField(null=True, blank=True, upload_to="post/")
    file = models.FileField(null=True, blank=True, upload_to="post/")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post')

    def __str__(self):
        return f"{self.created_at}"



