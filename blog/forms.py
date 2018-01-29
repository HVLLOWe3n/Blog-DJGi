from django import forms
from .models import Post


class PostForm(forms.ModelForm):    # Класс для формы

    class Meta:                     # Определяем какая модель будет использоватся для создания формы
        model = Post
        fields = ('title', 'text',)
