from django import forms
from django.core.validators import RegexValidator


class ComingSoonForm(forms.Form):
    email = forms.EmailField(
        label='ایمیل',
        max_length=255,
        min_length=5,
        widget=forms.EmailInput(attrs={
            'placeholder': 'ایمیل خود را وارد کنید',
            'class': 'form-control',
        }),
    )


class AdvertisingForm(forms.Form):
    phone = forms.CharField(
        label='تلفن همراه',
        min_length=11,
        max_length=11,
        widget=forms.TextInput(attrs={
            'class': 'form-clt',
            'placeholder': 'تلفن همراه شما',
        }),
        validators=[
            RegexValidator(
                regex=r'^09\d{9}$',
                message='تلفن همراه خود را درست وارد کنید!'
            )
        ],
    )
