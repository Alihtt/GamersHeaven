from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=250, verbose_name="نام دسته بندی")
    url_title = models.CharField(max_length=250, verbose_name="عنوان در url", unique=True)
    is_active = models.BooleanField(verbose_name="فعال / غیرفعال", default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "دسته بندی مقاله"
        verbose_name_plural = "دسته بندی مقالات"


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles', verbose_name='نویسنده')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True,
                                 verbose_name="دسته بندی")
    title = models.CharField(max_length=200, verbose_name='عنوان')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='اسلاگ')
    short_description = models.CharField(max_length=250, verbose_name="توضیحات کوتاه")
    description = models.TextField(verbose_name='توضیحات')
    image = models.ImageField(upload_to='blog', null=True, verbose_name='تصویر')
    is_active = models.BooleanField(verbose_name="فعال / غیرفعال")
    updated = models.DateField(auto_now=True, verbose_name='تاریخ بروزرسانی')
    created = models.DateField(auto_now_add=True, verbose_name='تاریخ ساخت')

    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"

    def __str__(self):
        return f'{self.title} {self.updated}'
