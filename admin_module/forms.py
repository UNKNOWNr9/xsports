from django import forms


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


class ResetPasswordForm(forms.Form):
    old_password = forms.CharField(
        label='کلمه عبور قبلی',
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