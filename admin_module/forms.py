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