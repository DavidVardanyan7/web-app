from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text', 'date']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name of articles'

            }),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Anons of articles'
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'publication date'
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Text of articles'
            }),


        }
