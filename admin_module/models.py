from django.db import models
from django.core.validators import RegexValidator


class AuthorRequest(models.Model):
    phone_validator = RegexValidator(
        regex=r'^09\d{9}$',
        message='شماره تلفن باید با 09 شروع شود و 11 رقم باشد.'
    )

    full_name = models.CharField(max_length=128, verbose_name='نام و نام خانوادگی')
    age = models.CharField(max_length=2, verbose_name='سن')
    city = models.CharField(max_length=20, verbose_name='محل سکونت')
    phone = models.CharField(
        max_length=11,
        verbose_name='شماره تلفن',
        validators=[RegexValidator(regex=r'^09\d{9}$', message='شماره تلفن باید با 09 شروع شود و 11 رقم باشد.')]
    )
    resume = models.TextField(verbose_name='متن درخواست شما')
    email = models.EmailField(max_length=128, verbose_name='ایمیل')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'درخواست نویسندگی'
        verbose_name_plural = 'درخواست های نویسندگی'
