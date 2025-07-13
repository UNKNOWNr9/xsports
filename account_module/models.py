from django.db import models
from django.contrib.auth.models import AbstractUser


class CostumeUser(AbstractUser):
    avatar = models.ImageField(upload_to='user_avatar', null=True, blank=True, verbose_name='تصویر پروفایل')
    email_active_code = models.CharField(max_length=100, verbose_name='کد فعالسازی')
    about_user = models.TextField(max_length=1000, verbose_name='درباره کاربر', default='درباره خودت یه چیزی بنویس که بقیه ببینن!')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'


