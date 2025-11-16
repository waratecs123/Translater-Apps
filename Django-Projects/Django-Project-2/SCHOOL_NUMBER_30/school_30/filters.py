import django_filters
from .models import News
from .models import MAIN_CATEGORIES, AUDIENCE_CATEGORIES, THEMATIC_CATEGORIES


class NewsFilter(django_filters.FilterSet):
    # Фильтр по основной категории
    main_category = django_filters.ChoiceFilter(
        choices=MAIN_CATEGORIES,
        label='Основная категория',
        empty_label='Все категории'
    )

    # Фильтр по аудитории
    audience_category = django_filters.ChoiceFilter(
        choices=AUDIENCE_CATEGORIES,
        label='Для кого',
        empty_label='Для всех'
    )

    # Фильтр по тематической категории
    thematic_category = django_filters.ChoiceFilter(
        choices=THEMATIC_CATEGORIES,
        label='Тематика',
        empty_label='Все тематики'
    )

    # Фильтр по дате (диапазон дат)
    created_at = django_filters.DateFromToRangeFilter(
        label='Дата публикации (от - до)',
        widget=django_filters.widgets.RangeWidget(attrs={'type': 'date'})
    )

    class Meta:
        model = News
        fields = ['main_category', 'audience_category', 'thematic_category', 'created_at']