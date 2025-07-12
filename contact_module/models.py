from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator


class ContactUs(models.Model):
    full_name = models.CharField(
        max_length=50,
        validators=[MinLengthValidator(6, message='نام خود را کامل وارد کنید')],
        verbose_name='نام و نام خانوادگی'
    )
    subject = models.CharField(max_length=100, verbose_name='موضوع پیام')
    message = models.TextField(verbose_name='پیام')
    phone = models.CharField(
        max_length=11,
        validators=[
            RegexValidator(regex=r'^09\d{9}$', message="شماره تلفن باید با 09 شروع شود و شامل ۱۱ رقم باشد."),
        ],
        verbose_name='تلفن همراه',
    )
    email = models.EmailField(
        max_length=255,
        validators=[
            MinLengthValidator(5, message='یک ایمیل معتبر وارد کنید!'),
        ],
        verbose_name='ایمیل'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    response = models.TextField(null=True, blank=True, verbose_name='پاسخ ادمین')
    is_read_by_admin = models.BooleanField(default=False, verbose_name='خاتمه')

    class Meta:
        verbose_name = 'تماس با ما'
        verbose_name_plural = 'تماس با ما'

    def __str__(self):
        return self.email
