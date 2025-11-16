from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(max_length=100, blank=False, unique=True)
    username = models.CharField(max_length=100, unique=True, blank=False)
    is_verified = models.BooleanField(default=False)
    verification_code = models.CharField(max_length=20, blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)


class Advert(models.Model):
    CATEGORY_CHOICES = [
        ('Tanks', 'Танки'),
        ('Heals', 'Хилы'),
        ('DD', 'ДД'),
        ('Merchants', 'Торговцы'),
        ('Guildmasters', 'Гилдмастеры'),
        ('Questgivers', 'Квестгиверы'),
        ('Blacksmiths', 'Кузнецы'),
        ('Tanners', 'Кожевники'),
        ('Potionmakers', 'Зельевары'),
        ('Spellmasters', 'Мастера заклинаний'),
    ]
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='adverts')
    title = models.CharField(max_length=255)
    content = models.TextField(blank=False)
    category = models.CharField(choices=CATEGORY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='adverts/', null=True, blank=True)
    video_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return (f"{self.title}"
                f"{self.created_at}"
                f"{self.author}")


class Response(models.Model):
    advert = models.ForeignKey(Advert, on_delete=models.CASCADE, related_name='responses')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    is_accepted = models.BooleanField(default=False)

    def __str__(self):
        return f"Отклик на {self.advert.title} от {self.author.username}"


class Newsletter(models.Model):
    title = models.CharField(max_length=200, blank=False)
    content = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    sent_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return (f"{self.user}"
                f"{self.is_active}")


class Media(models.Model):
    file = models.FileField(null=True, blank=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    advert = models.ForeignKey(Advert, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.uploaded_by}"