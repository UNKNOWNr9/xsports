from django.db import models

from account_module.models import CustomUser


class ArticleManager(models.Manager):
    def published(self):
        return self.filter(status=Article.STATUS.PUBLISHED)

    def draft(self):
        return self.filter(status=Article.STATUS.DRAFT)

    def investigation(self):
        return self.filter(status=Article.STATUS.INVESTIGATION)

    def rejected(self):
        return self.filter(status=Article.STATUS.REJECTED)


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
    class STATUS(models.TextChoices):
        DRAFT = 'DF', 'پیشنویس'
        PUBLISHED = 'PB', 'منتشرشده'
        REJECTED = 'RJ', 'رد شده'
        INVESTIGATION = 'IN', 'در حال بررسی'

    title = models.CharField(max_length=100, verbose_name='عنوان')
    image = models.ImageField(upload_to='article_images', verbose_name='تصویر')
    content = models.TextField(verbose_name='توضیحات')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    slug = models.SlugField(unique=True, verbose_name='آدرس')
    status = models.CharField(max_length=25, default=STATUS.DRAFT, verbose_name='وضعیت')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='نویسنده')
    selected_category = models.ForeignKey(ArticleCategory, on_delete=models.CASCADE, verbose_name='دسته بندی ها',
                                          related_name='article_category')
    objects = ArticleManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'پست'
        verbose_name_plural = 'پست ها'


class ArticleComments(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name="مقاله")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='نویسنده')
    message = models.TextField(verbose_name='متن پیام')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ انتشار')
    is_active = models.BooleanField(default=False, verbose_name='قبول شده / رد شده')

    def __str__(self):
        return str(self.article)

    class Meta:
        verbose_name = 'کامنت'
        verbose_name_plural = 'کامنت ها'


