from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models


class ComingSoon(models.Model):
    email = models.EmailField(
        max_length=255,
        validators=[
            MinLengthValidator(5, message='یک ایمیل معتبر وارد کنید!'),
        ],
        verbose_name='ایمیل',
    )

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'ایمیل'
        verbose_name_plural = 'ایمیل ها'


class Advertising(models.Model):
    phone = models.CharField(
        max_length=11,
        validators=[
            RegexValidator(regex=r'^09\d{9}$', message="شماره تلفن باید با 09 شروع شود و شامل ۱۱ رقم باشد."),
        ],
        verbose_name='تلفن همراه',
    )

    def __str__(self):
        return self.phone

    class Meta:
        verbose_name = 'تلفن مشتری'
        verbose_name_plural = 'تلفن مشتری ها'