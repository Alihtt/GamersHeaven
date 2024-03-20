from rest_framework.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.HomeArticlesList.as_view(), name='home'),
]
