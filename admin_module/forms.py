from django import forms
from django.core.exceptions import ValidationError


class EditProfileForm(forms.Form):
    first_name = forms.CharField(
        label='نام',
        min_length=3,
        max_length=50,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'نام خود را وارد کنید',
        }),
    )

    last_name = forms.CharField(
        label='نام خانوادگی',
        min_length=3,
        max_length=50,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'نام خانوادگی خود را وارد کنید',
        }),
    )

    about_user = forms.CharField(
        label='درباره شما',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'درباره خودتان یک پیامی بنویسید',
        })
    )

    avatar = forms.FileField(
        required=False,
        label='آواتار',
        widget=forms.FileInput(attrs={
            'class': 'custom-file-input',
        })
    )


class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(
        label='کلمه عبور فعلی',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'کلمه عبور فعلی را وارد کنید',
        })
    )

    new_password = forms.CharField(
        label='کلمه عبور جدید',
        max_length=128,
        min_length=8,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'کلمه عبور جدید خود را وارد کنید',
        })
    )

    confirm_password = forms.CharField(
        label='تکرار کلمه عبور',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'کلمه عبور جدید خود را تکرار کنید'
        })
    )

    def clean_confirm_password(self):
        new_password = self.cleaned_data.get('new_password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if new_password == confirm_password:
            return new_password
        else:
            raise ValidationError('تکرار کلمه عبور اشتباه است')
