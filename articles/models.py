from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse


class Category(models.Model):
    title = models.CharField(max_length=250, verbose_name="نام دسته بندی")
    url_title = models.CharField(max_length=250, verbose_name="عنوان در url", unique=True)
    sub_category = models.ForeignKey('self', related_name='categories', verbose_name='زیر مجموعه', null=True,
                                     blank=True, on_delete=models.CASCADE)
    is_sub = models.BooleanField(verbose_name="زیر مجموعه / مجموعه", default=False)
    is_active = models.BooleanField(verbose_name="فعال / غیرفعال", default=True)

    def __str__(self):
        return f'{self.id}-{self.title}'

    class Meta:
        verbose_name = "دسته بندی مقاله"
        verbose_name_plural = "دسته بندی مقالات"


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='uarticles', verbose_name='نویسنده')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, related_name='carticles',
                                 verbose_name="دسته بندی")
    title = models.CharField(max_length=200, verbose_name='عنوان')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='اسلاگ')
    short_description = models.CharField(max_length=250, verbose_name="توضیحات کوتاه")
    description = models.TextField(verbose_name='توضیحات')
    image = models.ImageField(upload_to='blog', null=True, blank=True, verbose_name='تصویر')
    is_active = models.BooleanField(verbose_name="فعال / غیرفعال")
    updated = models.DateField(auto_now=True, verbose_name='تاریخ بروزرسانی')
    created = models.DateField(auto_now_add=True, verbose_name='تاریخ ساخت')

    class Meta:
        ordering = ['-created']
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"

    def __str__(self):
        return f'{self.title} {self.updated}'

    def get_absolute_url(self):
        return reverse('articles:article-detail', args=[self.id, self.slug])
