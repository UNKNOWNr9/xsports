from django import forms


class ContactUsForm(forms.Form):
    SUBJECT_CHOICE = (
        ('', 'انتخاب کنید'),
        ('پیشنهاد', 'پیشنهاد'),
        ('انتقاد', 'انتقاد'),
        ('شکایات', 'شکایات'),
    )

    full_name = forms.CharField(
        label='نام و نام خانوادگی',
        min_length=6,
        max_length=50,
        error_messages={
            'min_length': 'نام و نام خانوادگی خود را کامل وارد کنید',
            'max_length': 'نام و نام خانوادگی خود را کامل وارد کنید',
        },
        widget=forms.TextInput(attrs={
            'class': 'form-clt',
            'placeholder': 'نام شما'
        }),
    )

    phone = forms.CharField(
        label='تلفن همراه',
        min_length=11,
        max_length=11,
        error_messages={
            'min_length': 'تلفن همراه خود را به درستی وارد کنید',
            'max_length': 'تلفن همراه خود را به درستی وارد کنید',
        },
        widget=forms.TextInput(attrs={
            'class': 'form-clt',
            'placeholder': 'تلفن همراه شما',
        }),
    )

    email = forms.EmailField(
        label='ایمیل',
        max_length=254,
        error_messages={
            'max_length': 'یک ایمیل معتبر وارد کنید'
        },
        widget=forms.EmailInput(attrs={
            'class': 'form-clt',
            'placeholder': 'ایمیل شما',
        }),
    )

    message = forms.CharField(
        label='پیام شما',
        min_length=30,
        error_messages={
            'min_length': 'پیام شما خیلی کوتاه است'
        },
        widget=forms.Textarea(attrs={
            'class': 'col-lg-12',
            'placeholder': 'پیام شما',
        }),
    )

    subject = forms.ChoiceField(
        choices=SUBJECT_CHOICE,
        label='موضوع پیام',
        widget=forms.Select(attrs={
            'class': 'form-clt',
        }),
        error_messages={'required': 'موضوع پیام را انتخاب کنید.'},
    )
