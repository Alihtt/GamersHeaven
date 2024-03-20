from django.contrib import admin
from .models import Article, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"url_title": ["title"]}


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    raw_id_fields = ['author', 'category']
    prepopulated_fields = {"slug": ["title"]}
