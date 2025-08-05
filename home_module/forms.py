from django import forms

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