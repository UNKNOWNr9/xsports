from django.db import models
from account_module.models import CustomUser


class ArticleCategory(models.Model):
    title = models.CharField(max_length=25, unique=True, verbose_name='عنوان')
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیرفعال')
    slug = models.SlugField(unique=True, verbose_name='آدرس')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'


class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    image = models.ImageField(upload_to='article_images', verbose_name='تصویر')
    content = models.TextField(verbose_name='توضیحات')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    slug = models.SlugField(unique=True, verbose_name='آدرس')
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیرفعال')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='نویسنده')
    selected_category = models.ForeignKey(ArticleCategory, on_delete=models.CASCADE, verbose_name='دسته بندی ها')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'پست'
        verbose_name_plural = 'پست ها'
