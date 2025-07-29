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
        label='آواتار',
        widget=forms.FileInput(attrs={
            'class': 'custom-file-input',
        })
    )