from django import forms


class EditProfileForm(forms.Form):
    first_name = forms.CharField(
        label='نام',
        min_length=6,
        max_length=50,
        widget=forms.TextInput(attrs={
            'class': '',
            'placeholder': 'نام',
        }),
    )

    last_name = forms.CharField(
        label='نام',
        min_length=6,
        max_length=50,
        widget=forms.TextInput(attrs={
            'class': '',
            'placeholder': 'نام',
        }),
    )

    about_author = forms.CharField(
        label='درباره من',
        max_length=500,
        widget=forms.Textarea(attrs={
            'class': '',
            'placeholder': 'متن شما'
        })
    )