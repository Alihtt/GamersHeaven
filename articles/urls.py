from rest_framework.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.ArticleListCreate.as_view(), name='article-list'),
    path('<int:pk>/<slug:slug>/', views.ArticleDetail.as_view(), name='article-detail'),

]
