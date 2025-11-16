from django import forms
from .models import Feedback, Cooperation

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['title', 'email', 'surname', 'name', 'patronymic', 'nickname', 'text', 'photo']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 5}),
        }

class CooperationForm(forms.ModelForm):
    class Meta:
        model = Cooperation
        fields = ['title', 'phone', 'email', 'surname', 'name', 'patronymic', 'company', 'text', 'photo1', 'photo2']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 5}),
            'phone': forms.TextInput(attrs={'placeholder': '79XXXXXXXXX'}),
        }