from django import forms

from .models import ArticleComments


class ArticleCommentsForm(forms.ModelForm):
    class Meta:
        model = ArticleComments
        fields = ['message']
        widgets = {
            'message': forms.Textarea(attrs={
                'class': 'form-clt',
                'rows': 4,
                'placeholder': 'پیام خود را وارد کنید'
            }),
        }

        labels = {
            'message': 'متن کامنت',
        }