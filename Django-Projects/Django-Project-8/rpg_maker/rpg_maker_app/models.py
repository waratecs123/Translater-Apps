from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Race(models.Model):
    NAMES_RACE = [
        ("EL", "Эльфы"),
        ("LD", "Люди"),
        ("GN", "Гномы"),
        ("OR", "Орки"),
        ("AN", "Энты"),
        ("TR", "Тролли"),
    ]
    name = models.CharField(choices=NAMES_RACE, default="EL", max_length=2, blank=False)
    description = models.TextField(max_length=3000, blank=False, default="Не задано")

    def __str__(self):
        return f"{self.name}"


class Class(models.Model):
    NAMES_CLASS = [
        ("VN", "Воины"),
        ("MG", "Маги"),
        ("UC", "Ученые"),
        ("RZ", "Разведчивы"),
        ("RM", "Ремесленники"),
        ("LD", "Лидеры"),
        ("ZM", "Земледельцы"),
    ]
    name = models.CharField(choices=NAMES_CLASS, default="VN", max_length=2, blank=False)
    description = models.TextField(max_length=3000, blank=False, default="Не задано")

    def __str__(self):
        return f"{self.name}"


class Skill(models.Model):
    NAMES_SKILL = [
        ("VM", "Владение Мечом"),
        ("VT", "Владение Топором"),
        ("VK", "Владение Копьем"),
        ("VL", "Владение Луком"),
        ("VH", "Владение Щитом"),
        ("VS", "Верховая Стрельба"),
        ("KB", "Конный Бой"),
        ("PP", "Поединок"),
        ("OD", "Осадное дело"),
        ("SN", "Свет Нуменора"),
        ("VV", "Внушение"),
        ("ZT", "Защита от Тьмы"),
        ("SG", "Свет Галадриэль"),
        ("ZD", "Заклинание Дверей"),
        ("CH", "Чернокнижие"),
        ("OO", "Обличение"),
        ("BP", "Бесшумное Передвижение"),
        ("MM", "Маскировка"),
        ("VC", "Выслеживание"),
        ("OM", "Ориентация на Местности"),
        ("VD", "Выживание в Дикой Природе"),
        ("SS", "Скрытность"),
        ("ZY", "Знание Языков"),
        ("ZI", "Знание Древней Истории"),
        ("KD", "Кузнечное дело"),
        ("CC", "Целительство"),
        ("TT", "Травничество"),
        ("PS", "Песнь и Слово"),
        ("KK", "Кораблестроение"),
        ("VO", "Вдохновляющее Лидерство"),
        ("DD", "Дипломатия"),
        ("TS", "Тактика и Стратегия"),
        ("MZ", "Мужество"),
        ("CI", "Сопротивление Искушению Властью"),
    ]
    name = models.CharField(choices=NAMES_SKILL, default="CI", max_length=2, blank=False)
    description = models.TextField(max_length=3000, blank=False, default="Не задано")

    def __str__(self):
        return f"{self.name}"


class Spell(models.Model):
    NAMES_SPELL = [
        ("ZS", "Заклинания Света и Защиты"),
        ("ZO", "Заклинания Огня и Разрушения"),
        ("ZV", "Заклинания Воды и Природы"),
        ("ZR", "Заклинания Разума и Иллюзий"),
        ("TM", "Темная Магия и Некромантия"),
        ("MS", "Магия Сотворения и Искусства"),
    ]
    name = models.CharField(choices=NAMES_SPELL, default="ZS", max_length=2, blank=False)
    description = models.TextField(max_length=3000, blank=False, default="Не задано")
    mana_cost = models.IntegerField(blank=False, default=0, validators=[MinValueValidator(0), MaxValueValidator(1000)])
    level_required = models.IntegerField(blank=False, default=0, validators=[MinValueValidator(0), MaxValueValidator(1000)])

    def __str__(self):
        return (f"{self.name}"
                f"{self.mana_cost}"
                f"{self.level_required}")


class Character(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=False)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    character_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    level = models.IntegerField(blank=False, validators=[MinValueValidator(0), MaxValueValidator(1000)], default=0)
    backstory = models.TextField(max_length=5000, blank=False)
    skill = models.ManyToManyField(Skill)
    spell = models.ManyToManyField(Spell)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f"{self.name}"
                f"{self.race}"
                f"{self.character_class}"
                f"{self.level}")


class Attribute(models.Model):
    CONSTITUTION = [
        ("NT", "Нормостенический тип"),
        ("GT", "Гиперстенический тип"),
        ("AT", "Астенический тип")
    ]
    character = models.OneToOneField(Character, on_delete=models.CASCADE)
    strength = models.IntegerField(blank=False, validators=[MinValueValidator(0), MaxValueValidator(1000)], default=0)
    dexterity = models.IntegerField(blank=False, validators=[MinValueValidator(0), MaxValueValidator(1000)], default=0)
    constitution = models.CharField(choices=CONSTITUTION, default="AT", max_length=2, blank=False)
    intelligence = models.IntegerField(blank=False, validators=[MinValueValidator(0), MaxValueValidator(1000)], default=0)
    wisdom = models.IntegerField(blank=False, validators=[MinValueValidator(0), MaxValueValidator(1000)], default=0)
    charisma = models.IntegerField(blank=False, validators=[MinValueValidator(0), MaxValueValidator(1000)], default=0)

    @property
    def health(self):
        if self.character.level <= 0:
            return 0
        else:
            return (self.character.level ** 2) // 2

    @property
    def mana(self):
        if self.intelligence <= 0 or self.character.level <= 0:
            return 0
        else:
            return (self.intelligence * self.character.level) // 2

    def __str__(self):
        return (f"{self.strength}"
                f"{self.dexterity}"
                f"{self.constitution}"
                f"{self.intelligence}"
                f"{self.wisdom}"
                f"{self.charisma}"
                f"{self.health}"
                f"{self.mana}")


class Type(models.Model):
    NAMES_TYPE = [
        ("OR", "Оружие"),
        ("BR", "Броня"),
        ("ZL", "Зелья"),
        ("RS", "Растения"),
        ("KP", "Квестовые предметы"),
        ("AR", "Артефакты"),
    ]

    name = models.CharField(choices=NAMES_TYPE, max_length=2, default="AR", blank=False)

    def __str__(self):
        return f"{self.name}"


class Item(models.Model):
    NAMES_ITEM = [
        ("MC", "Меч"),
        ("KZ", "Кинжал"),
        ("TR", "Топор"),
        ("ML", "Молот"),
        ("KP", "Копье"),
        ("AL", "Алебарда"),
        ("LK", "Лук"),
        ("AR", "Арбалет"),
        ("PS", "Посох"),
        ("KC", "Кольчуга"),
        ("LD", "Латные доспехи"),
        ("ND", "Нагрудник"),
        ("SH", "Шлем"),
        ("CH", "Щит"),
        ("NR", "Наручи"),
        ("EP", "Эльфийский плащ"),
        ("ZZ", "Целебное зелье"),
        ("LT", "Лечебная трава"),
        ("YD", "Яд"),
        ("KL", "Ключ"),
        ("KR", "Карта"),
        ("PL", "Послание"),
        ("TK", "Токен"),
        ("SV", "Символ власти"),
        ("PR", "Предмет для ритуала"),
        ("KV", "Кольцо Власти"),
        ("LO", "Легендарное оружие"),
        ("SL", "Сильмарилл"),
        ("PP", "Палантир"),
    ]
    name = models.CharField(choices=NAMES_ITEM, default="PP", max_length=2, blank=False)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    description = models.TextField(max_length=3000, blank=False, default="Не задано")

    def __str__(self):
        return (f"{self.name}"
                f"{self.type}")


class InventoryItem(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=False, default=0, validators=[MinValueValidator(0), MaxValueValidator(1000)])
    is_equipped = models.BooleanField(blank=False, default=False)

    def __str__(self):
        return (f"{self.character}"
                f"{self.item}"
                f"{self.quantity}")







