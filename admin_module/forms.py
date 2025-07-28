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

    #TODO: make avatat field

    about_author = forms.CharField(
        label='درباره من',
        max_length=500,
        widget=forms.Textarea(attrs={
            'class': '',
            'placeholder': 'متن شما'
        })
    )