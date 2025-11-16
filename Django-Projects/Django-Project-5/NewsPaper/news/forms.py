from django import forms
from django.core.exceptions import ValidationError
from .models import Post
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group


class NewsForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'post_type', 'text', 'categories']
        widgets = {
            'post_type': forms.RadioSelect,
            'categories': forms.CheckboxSelectMultiple,
            'text': forms.Textarea(attrs={'rows': 5}),
        }
        labels = {
            'title': 'Заголовок',
            'post_type': 'Тип публикации',
            'text': 'Текст',
            'categories': 'Категории',
        }

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        text = cleaned_data.get('text')

        if title and text and title.lower() in text.lower():
            raise ValidationError("Заголовок не должен содержаться в тексте")

        return cleaned_data


class CustomSignupForm(SignupForm):
    def save(self, request):
        user = super().save(request)
        common_group = Group.objects.get_or_create(name='common')[0]
        user.groups.add(common_group)
        return user

class SubscribeForm(forms.Form):
    category_id = forms.IntegerField(widget=forms.HiddenInput())
