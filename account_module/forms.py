from django import forms
from django.core.exceptions import ValidationError


class RegisterForm(forms.Form):
    email = forms.EmailField(
        label='ایمیل',
        max_length=255,
        min_length=6,
        widget=forms.EmailInput(attrs={
            'placeholder': 'ایمیل خود را وارد کنید',
            'class': 'input100',
            'autocomplete': 'off',
        }),
        error_messages={
            'min_length': 'یک ایمیل معتر وارد کنید',
            'max_length': 'یک ایمیل معتر وارد کنید',
        }
    )

    password = forms.CharField(
        label='کلمه عبور',
        max_length=128,
        min_length=8,
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'new-password',
            'class': 'input100',
            'placeholder': 'کلمه عبور خود را وارد کنید',
        }),
        error_messages={
            'min_length': 'یک کلمه عبور معتبر وارد کنید',
            'max_length': 'یک کلمه عبور معتبر وارد کنید',
        }
    )

    confirm_password = forms.CharField(
        label='تکرار کلمه عبور',
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'new-password',
            'class': 'input100',
            'placeholder': 'کلمه عبور خود را تکرار کنید',
        }),
    )

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password == confirm_password:
            return confirm_password
        else:
            raise ValidationError('confirm_password' 'تکرار کلمه عبور اشتباه است')