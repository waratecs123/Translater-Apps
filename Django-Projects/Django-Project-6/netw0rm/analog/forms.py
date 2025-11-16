from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['category', 'nickname', 'text', 'photo', 'file']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['nickname', 'text', 'photo', 'file']
