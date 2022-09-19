from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    title = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': "Your title"}))
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'article',
                'rows': 20,
                'columns': 120
            }
        )
    )
    active = forms.BooleanField()

    class Meta:
        model = Article
        fields = [
            'title',
            'content',
            'active'
        ]
