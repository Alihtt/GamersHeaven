from rest_framework.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.ArticleList.as_view(), name='article-list'),
    path('<int:pk>/<slug:slug>/', views.ArticleDetail.as_view(), name='article-detail'),
    path('categories/', views.CategoryList.as_view(), name='category-list'),

]
