from django import forms
from .models import ArticleComments


class ArticleCommentsForm(forms.ModelForm):
    class Meta:
        model = ArticleComments
        fields = ['name', 'body']
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-clt', 'rows': 4}),
        }
        labels = {
            'body': 'متن کامنت',
        }