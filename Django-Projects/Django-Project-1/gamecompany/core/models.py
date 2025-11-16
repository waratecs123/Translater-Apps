from django.db import models

# Create your models here.
class Games(models.Model):
    title = models.CharField(max_length=255, blank=False, unique=True)
    company = models.CharField(max_length=255, blank=False)
    text = models.TextField(blank=False)
    year =  models.IntegerField(blank=False)
    trailer = models.URLField(max_length=255, blank=True)
    photo1 = models.ImageField(blank=True, null=True, upload_to='games/')
    photo2 = models.ImageField(blank=True, null=True, upload_to='games/')
    photo3 = models.ImageField(blank=True, null=True, upload_to='games/')
    presentation = models.FileField(upload_to='presentation/', blank=True, null=True)
    document1 = models.FileField(upload_to='document/', blank=True, null=True)
    document2 = models.FileField(upload_to='document/', blank=True, null=True)
    document3 = models.FileField(upload_to='document/', blank=True, null=True)

    def __str__(self):
        return (f"{self.title}"
                f"{self.year}"
                f"{self.company}")


POSITION_CHOICES = [
    ('GD', 'Геймдизайнер'),
    ('LD', 'Ведущий геймдизайнер'),
    ('NLD', 'Нарративный дизайнер'),
    ('LVLD', 'Левел-дизайнер'),
    ('PD', 'Продуктовый дизайнер'),
    ('PRG', 'Программист'),
    ('CPRG', 'Ведущий программист'),
    ('GPRG', 'Геймплей-программист'),
    ('GPRG', 'Графический программист'),
    ('TPRG', 'Инструментальный программист'),
    ('AI', 'Программист ИИ'),
    ('ART', 'Художник'),
    ('CART', 'Арт-директор'),
    ('2D', '2D-художник'),
    ('3D', '3D-художник'),
    ('CHAR', 'Художник по персонажам'),
    ('ENV', 'Художник окружения'),
    ('VFX', 'Художник VFX'),
    ('TECHART', 'Технический художник'),
    ('ANIM', 'Аниматор'),
    ('CANIM', 'Ведущий аниматор'),
    ('SND', 'Звукорежиссер'),
    ('COMP', 'Композитор'),
    ('VA', 'Режиссер озвучки'),
    ('QA', 'Тестировщик'),
    ('LEADQA', 'Ведущий тестировщик'),
    ('AQA', 'Автоматизатор тестирования'),
    ('PM', 'Продюсер'),
    ('APM', 'Ассоциированный продюсер'),
    ('SPM', 'Старший продюсер'),
    ('MKT', 'Маркетолог'),
    ('CM', 'Менеджер комьюнити'),
    ('SM', 'Соцмедиа менеджер'),
    ('HR', 'HR-специалист'),
    ('RECR', 'Рекрутер'),
    ('ADM', 'Администратор'),
    ('ACC', 'Бухгалтер'),
    ('LAW', 'Юрист'),
    ('CEO', 'Генеральный директор'),
    ('CTO', 'Технический директор'),
    ('COO', 'Операционный директор'),
    ('CFO', 'Финансовый директор'),
]

class Staff(models.Model):
    surname = models.CharField(max_length=255, blank=False)
    name = models.CharField(max_length=255, blank=False)
    patronymic = models.CharField(max_length=255, blank=True)
    year = models.IntegerField(blank=False)
    position = models.CharField(max_length=10, default="PRG", choices=POSITION_CHOICES)
    photo = models.ImageField(null=True, blank=True, upload_to='staff/')
    experience = models.IntegerField(blank=False)
    about = models.TextField(max_length=1500, blank=False)

    @property
    def full_name(self):
        return f"{self.surname} {self.name} {self.patronymic}"

    def __str__(self):
        return (f"{self.full_name}"
                f"{self.year}"
                f"{self.position}")


class Feedback(models.Model):
    title = models.CharField(blank=False, max_length=255)
    email = models.EmailField(blank=False, unique=True, max_length=100)
    surname = models.CharField(max_length=255, blank=False)
    name = models.CharField(max_length=255, blank=False)
    patronymic = models.CharField(max_length=255, blank=True)
    nickname = models.CharField(max_length=255, blank=True)
    text = models.TextField(blank=False, max_length=5000)
    photo = models.ImageField(blank=True, null=True, upload_to="feedback/")


EXPERIENCE_LEVEL_CHOICES = [
    ('TRAINEE', 'Трени'),
    ('INTERN', 'Интерн'),
    ('JUNIOR', 'Джуниор'),
    ('JUNIOR+', 'Джуниор+'),
    ('MIDDLE', 'Миддл'),
    ('MIDDLE+', 'Миддл+'),
    ('SENIOR', 'Сеньор'),
    ('SENIOR+', 'Сеньор+'),
    ('LEAD', 'Лид'),
    ('SLEAD', 'Старший лид'),
    ('ARCHITECT', 'Архитектор'),
    ('PM', 'Менеджер проекта'),
    ('HOD', 'Руководитель отдела'),
    ('DIRECTOR', 'Директор'),
]

RELEVANCE_CHOICES = [
    ('ACTIVE', 'Актуально'),
    ('INACTIVE', 'Неактуально'),
    ('ARCHIVED', 'В архиве'),
    ('DRAFT', 'Черновик'),
]

class Vacancy(models.Model):
    title = models.CharField(blank=False, max_length=255)
    text = models.TextField(max_length=2000, blank=False)
    experience = models.IntegerField(blank=False)
    price = models.IntegerField(blank=False)
    experience_level = models.CharField(choices=EXPERIENCE_LEVEL_CHOICES, default="JUNIOR", max_length=20)
    is_actual = models.CharField(choices=RELEVANCE_CHOICES, max_length=15, default="DRAFT")
    photo1 = models.ImageField(null=False, blank=False)
    photo2 = models.ImageField(null=True, blank=True)
    phone = models.CharField(blank=False)
    email = models.EmailField(blank=False, max_length=100)

    @property
    def full_phone(self):
        cleaned_phone = self.phone
        return f"+7 ({cleaned_phone[1:4]}) {cleaned_phone[4:7]}-{cleaned_phone[7:9]}-{cleaned_phone[9:]}"

    def __str__(self):
        return (f"{self.title}"
                f"{self.is_actual}")


class Products(models.Model):
    name = models.CharField(blank=False, unique=True)
    about = models.TextField(max_length=2000, blank=False, unique=True)
    price = models.IntegerField(blank=False)
    quantity = models.IntegerField(blank=False)
    photo = models.ImageField(upload_to="products/", null=False, blank=False)
    urls = models.URLField(max_length=1000, blank=False, unique=True)

    def __str__(self):
        return (f"{self.name}"
                f"{self.price}")


class News(models.Model):
    title = models.CharField(max_length=255, blank=False)
    text = models.TextField(max_length=5000, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    photo1 = models.ImageField(upload_to="news/", null=False, blank=False)
    photo2 = models.ImageField(upload_to="news/", null=True, blank=True)
    photo3 = models.ImageField(upload_to="news/", null=True, blank=True)

    def __str__(self):
        return (f"{self.title}"
                f"{self.created_at}")


class Cooperation(models.Model):
    title = models.CharField(blank=False, max_length=255)
    phone = models.IntegerField(blank=False)
    email = models.EmailField(blank=False, unique=True, max_length=100)
    surname = models.CharField(max_length=255, blank=False)
    name = models.CharField(max_length=255, blank=False)
    patronymic = models.CharField(max_length=255, blank=True)
    company = models.CharField(max_length=255, blank=True)
    text = models.TextField(blank=False, max_length=5000)
    photo1 = models.ImageField(blank=True, null=True, upload_to="cooperation/")
    photo2 = models.ImageField(blank=True, null=True, upload_to="cooperation/")

    @property
    def full_phone(self):
        cleaned_phone = self.phone
        return f"+7 ({cleaned_phone[1:4]}) {cleaned_phone[4:7]}-{cleaned_phone[7:9]}-{cleaned_phone[9:]}"

    def __str__(self):
        return (f"{self.title}"
                f"{self.company}"
                f"{self.phone}")


class Sponsors(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=True)
    about = models.TextField(max_length=3000, blank=False, unique=True)
    photo = models.ImageField(upload_to="sponsors/", blank=False, null=False)
    surname_d = models.CharField(blank=False, max_length=255)
    name_d = models.CharField(blank=False, max_length=255)
    patronymic_d = models.CharField(blank=False, max_length=255)
    year = models.IntegerField(blank=False)
    financing = models.IntegerField(blank=False)
    url = models.URLField(max_length=1000, blank=False)

    @property
    def full_name_director(self):
        return f"{self.surname_d} {self.name_d} {self.patronymic_d}"

    def __str__(self):
        return (f"{self.name}"
                f"{self.full_name_director}"
                f"{self.financing}")