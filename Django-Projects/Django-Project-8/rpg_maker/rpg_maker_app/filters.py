import django_filters
from .models import Character, Attribute, InventoryItem, Race, Class, Spell, Skill, Item


class CharacterFilterSet(django_filters.FilterSet):
    name_filter = django_filters.CharFilter(
        field_name='name',
        lookup_expr='icontains',
        label='Имя персонажа'
    )
    race_filter = django_filters.ModelChoiceFilter(
        field_name='race',
        queryset=Race.objects.all(),
        label='Раса',
        empty_label='Все расы'
    )
    class_filter = django_filters.ModelChoiceFilter(
        field_name='character_class',
        queryset=Class.objects.all(),
        label='Класс',
        empty_label='Все классы'
    )
    level_filter = django_filters.NumberFilter(
        field_name='level',
        lookup_expr='exact',
        label='Уровень равный'
    )
    backstory_filter = django_filters.CharFilter(
        field_name='backstory',
        lookup_expr='istartswith',
        label='История'
    )
    skill_filter = django_filters.ModelMultipleChoiceFilter(
        field_name='skill',
        queryset=Skill.objects.all(),
        label='Умения',
        conjoined=False,
    )
    spell_filter = django_filters.ModelMultipleChoiceFilter(
        field_name='spell',
        queryset=Spell.objects.all(),
        label='Заклинания',
        conjoined=False,
    )
    created_at_filter = django_filters.DateFilter(
        field_name='created_at',
        lookup_expr='gte',
        label='Дата создания после'
    )
    class Meta:
        model = Character
        fields = []


class AttributeFilterSet(django_filters.FilterSet):
    character_filter = django_filters.ModelChoiceFilter(
        field_name='character',
        queryset=Character.objects.all(),
        label='Имя персонажа',
        empty_label='Все персонажи',
    )
    strength_filter = django_filters.NumberFilter(
        field_name='strength',
        lookup_expr='gte',
        label='Сила больше или равна'
    )
    dexterity_filter = django_filters.NumberFilter(
        field_name='dexterity',
        lookup_expr='gte',
        label='Ловкость больше или равна'
    )
    constitution_filter = django_filters.ChoiceFilter(
        field_name='constitution',
        choices=Attribute.CONSTITUTION,
        label='Телосложение',
        empty_label='Все телосложения'
    )
    intelligence_filter = django_filters.NumberFilter(
        field_name='intelligence',
        lookup_expr='gte',
        label='Интеллект больше или равен'
    )
    wisdom_filter = django_filters.NumberFilter(
        field_name='wisdom',
        lookup_expr='gte',
        label='Мудрость больше или равна'
    )
    charisma_filter = django_filters.NumberFilter(
        field_name='charisma',
        lookup_expr='gte',
        label='Харизма больше или равна'
    )
    class Meta:
        model = Attribute
        fields = []


class InventoryItemFilterSet(django_filters.FilterSet):
    character_filter = django_filters.ModelChoiceFilter(
        field_name='character',
        queryset=Character.objects.all(),
        label='Имя персонажа',
        empty_label='Все персонажи',
    )
    item_filter = django_filters.ModelChoiceFilter(
        field_name='item',
        queryset=Item.objects.all(),
        label='Объект',
        empty_label='Все объекты'
    )
    quantity_filter = django_filters.NumberFilter(
        field_name='quantity',
        lookup_expr='gte',
        label='Количество больше или равно'
    )
    is_equipped_filter = django_filters.BooleanFilter(
        field_name='is_equipped',
        label='Одет ли предмет'
    )
    class Meta:
        model = InventoryItem
        fields = []
