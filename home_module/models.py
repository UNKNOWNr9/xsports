from django.core.validators import MinLengthValidator
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