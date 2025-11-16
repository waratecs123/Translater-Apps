from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

MAIN_CATEGORIES = (
    ('Ads', 'Объявления'),
    ('Special Events', 'Мероприятия'),
    ('Common events', 'Общие события')
)

AUDIENCE_CATEGORIES = (
    ('For parents', 'Для родителей'),
    ('For students', 'Для учеников'),
    ('For teachers', 'Для учителей'),
)

THEMATIC_CATEGORIES = (
    ('Sport', 'Спорт'),
    ('Science', 'Наука'),
    ('Creation', 'Творчество'),
    ('Safety', 'Безопасность')
)

STATUS = (
    ('Yes', 'Решено'),
    ('No', 'Не решено')
)

class News(models.Model):
    heading = models.CharField(max_length=100, blank=False, unique=True)
    photo = models.ImageField(upload_to='news/', null=True, blank=True)
    text = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    main_category = models.CharField(choices=MAIN_CATEGORIES, default='Общие события', blank=False)
    audience_category = models.CharField(choices=AUDIENCE_CATEGORIES, default='Для учеников', blank=False)
    thematic_category = models.CharField(choices=THEMATIC_CATEGORIES, default='Наука', blank=False)

    @property
    def not_full_text(self):
        return f"{self.text[:100]}..."

    def __str__(self):
        return (f"{self.heading}"
                f"{self.photo}"
                f"{self.text}"
                f"{self.created_at}"
                f"{self.main_category}"
                f"{self.audience_category}"
                f"{self.thematic_category}")


class Subjects(models.Model):
    title = models.CharField(max_length=50, blank=False)


class Position(models.Model):
    title = models.CharField(max_length=120, blank=False)


class Staff(models.Model):
    surname = models.CharField(max_length=50, blank=False)
    name = models.CharField(max_length=50, blank=False)
    patronymic = models.CharField(max_length=50, blank=False)
    photo = models.ImageField(upload_to='photo_teacher/', null=True, blank=True)
    position = models.ManyToManyField(Position, blank=False)
    email = models.EmailField(blank=True)
    phone = models.CharField(blank=False)
    telegram = models.CharField(max_length=50, blank=True)
    room = models.IntegerField()
    education = models.TextField(blank=False)
    qualification = models.CharField(max_length=70, blank=False)
    subjects = models.ManyToManyField(Subjects, blank=False)
    work_experience = models.IntegerField()
    short_bio = models.TextField(max_length=500, blank=False)

    @property
    def full_name(self):
        return f"{self.surname} {self.name} {self.patronymic}"

    @property
    def full_phone(self):
        cleaned_phone = self.phone
        return f"+7 ({cleaned_phone[1:4]}) {cleaned_phone[4:7]}-{cleaned_phone[7:9]}-{cleaned_phone[9:]}"

    def __str__(self):
        return (f"{self.full_name}"
                f"{self.photo}"
                f"{self.position}"
                f"{self.email}"
                f"{self.full_phone}"
                f"{self.telegram}"
                f"{self.room}"
                f"{self.education}"
                f"{self.qualification}"
                f"{self.subjects}"
                f"{self.work_experience}"
                f"{self.short_bio}")


class Feedback(models.Model):
    title = models.CharField(max_length=150, blank=False)
    nickname = models.CharField(max_length=100, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(blank=False)
    mail = models.EmailField(blank=False, default="no-email@example.com")
    text = models.TextField(blank=False)
    status = models.CharField(choices=STATUS, default='Не решено')

    @property
    def full_phone(self):
        cleaned_phone = self.phone
        return f"+7 ({cleaned_phone[1:4]}) {cleaned_phone[4:7]}-{cleaned_phone[7:9]}-{cleaned_phone[9:]}"

    def __str__(self):
        return (f"{self.title}"
                f"{self.nickname}"
                f"{self.created_at}"
                f"{self.full_phone}"
                f"{self.text}")

class SchoolDocument(models.Model):
    heading = models.CharField(max_length=120, blank=False, unique=True)
    text = models.TextField(blank=False)
    photo = models.ImageField(upload_to='documents/', blank=True, null=True)

    def __str__(self):
        return (f"{self.heading}"
                f"{self.text}"
                f"{self.photo}")

ACTUAL = (
    ('yes', 'Да'),
    ('no', 'Нет')
)


class Vacancy(models.Model):
    heading = models.CharField(max_length=120, blank=False)
    salary = models.IntegerField(blank=False)
    text = models.TextField(blank=False)
    is_actual = models.CharField(choices=ACTUAL, max_length=3, default='Да')

    def __str__(self):
        return (f"{self.heading}"
                f"{self.salary}"
                f"{self.text}"
                f"{self.is_actual}")


class Sponsors(models.Model):
    heading = models.CharField(max_length=255, blank=False, unique=True)
    about = models.TextField(blank=False)

    def __str__(self):
        return (f"{self.heading}"
                f"{self.about}")