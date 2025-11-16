from django.db import models
from django.core.validators import EmailValidator, RegexValidator


class User(models.Model):
    email = models.EmailField(unique=True, validators=[EmailValidator()])
    phone = models.CharField(max_length=10, blank=False)
    last_name = models.CharField(max_length=100, verbose_name="Фамилия", blank=False)
    first_name = models.CharField(max_length=100, verbose_name="Имя", blank=False)
    patronymic = models.CharField(max_length=100, blank=True, verbose_name="Отчество",)

    @property
    def full_phone(self):
        return f"+7 ({self.phone[0:3]}) {self.phone[3:6]}-{self.phone[6:8]}-{self.phone[8:10]}"

    @property
    def full_name(self):
        return f"{self.last_name} {self.first_name} {self.patronymic}"

    def __str__(self):
        return (f"{self.email}"
                f"{self.last_name}")


class Area(models.Model):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return (f"{self.parent}"
                f"{self.title}")

    class Meta:
        ordering = ['title']


class ActivityType(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.title}"


class Pereval(models.Model):
    STATUS_CHOICES = [
        ('new', 'Новый'),
        ('pending', 'На модерации'),
        ('accepted', 'Принят'),
        ('rejected', 'Отклонен'),
    ]

    beauty_title = models.CharField(max_length=255, blank=True)
    title = models.CharField(max_length=255)
    other_titles = models.CharField(max_length=255, blank=True)
    connect = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='new')
    add_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.SET_NULL, null=True)
    activities = models.ManyToManyField(ActivityType)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (f"{self.title}"
                f"{self.created_at}")


class Coord(models.Model):
    pereval = models.OneToOneField(Pereval, on_delete=models.CASCADE, related_name='coords')
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    height = models.IntegerField()

    def __str__(self):
        return (f"{self.latitude}"
                f"{self.height}")


class Level(models.Model):
    pereval = models.OneToOneField(Pereval, on_delete=models.CASCADE, related_name='level')
    winter = models.CharField(max_length=10, blank=True)
    summer = models.CharField(max_length=10, blank=True)
    autumn = models.CharField(max_length=10, blank=True)
    spring = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return (f"{self.winter}"
                f"{self.summer}"
                f"{self.autumn}"
                f"{self.spring}")


class Image(models.Model):
    pereval = models.ForeignKey(Pereval, on_delete=models.CASCADE, related_name='images')
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='pereval_images/')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f"{self.title}"
                f"{self.date_added}")

    class Meta:
        ordering = ['date_added']
