from django import forms
from .models import News, Feedback

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['heading', 'photo', 'text', 'main_category', 'audience_category', 'thematic_category']
        widgets = {
            'heading': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите заголовок новости'
            }),
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Текст новости...'
            }),
            'main_category': forms.Select(attrs={'class': 'form-control'}),
            'audience_category': forms.Select(attrs={'class': 'form-control'}),
            'thematic_category': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'heading': 'Заголовок',
            'photo': 'Изображение',
            'text': 'Текст новости',
            'main_category': 'Основная категория',
            'audience_category': 'Аудитория',
            'thematic_category': 'Тематика',
        }

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['title', 'nickname', 'phone', 'mail', 'text']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Тема обращения'
            }),
            'nickname': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваше имя'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+7 (XXX) XXX-XX-XX'
            }),
            'mail': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'email@example.com'
            }),
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Текст обращения...'
            }),
        }
        labels = {
            'title': 'Тема',
            'nickname': 'Имя',
            'phone': 'Телефон',
            'mail': 'Email',
            'text': 'Сообщение',
        }