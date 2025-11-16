from django_filters import FilterSet, CharFilter, ModelChoiceFilter, DateFilter
from django import forms
from .models import Post, Author


class NewsFilter(FilterSet):
    title = CharFilter(
        field_name='title',
        lookup_expr='icontains',
        label='Название',
        widget=forms.TextInput(attrs={'class': 'form-control'}))

    author = ModelChoiceFilter(
        field_name='author__user',
        queryset=Author.objects.all(),
        label='Автор',
        widget=forms.Select(attrs={'class': 'form-control'}))

    created_after = DateFilter(
        field_name='created_at',
        lookup_expr='gt',
        label='Опубликовано после',
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))

    class Meta:
        model = Post
        fields = []