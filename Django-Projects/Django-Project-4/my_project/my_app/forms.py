from django import forms
from .models import *


class ResponseFilterForm(forms.Form):
    advert_id = forms.ChoiceField(required=False)
    status = forms.ChoiceField(
        required=False,
        choices=[('', 'Все'), ('accepted', 'Принятые'), ('rejected', 'Отклоненные')]
    )

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.fields['advert_id'].choices = [('', 'Все')] + [
            (advert.id, advert.title) for advert in Advert.objects.filter(author=user)
        ]


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['title', 'content']