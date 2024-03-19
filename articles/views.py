from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from .serializers import ArticleSerializer, CategorySerializer
from .models import Article, Category
from .paginations import StandardResultsSetPagination


class CategoryList(ListAPIView):
    queryset = Category.objects.filter(is_active=True).all()
    serializer_class = CategorySerializer


class ArticleList(ListAPIView):
    queryset = Article.objects.filter(is_active=True).all()
    serializer_class = ArticleSerializer
    pagination_class = StandardResultsSetPagination


class ArticleDetail(APIView):
    def get(self, request, pk, slug):
        article = Article.objects.get(pk=pk, slug=slug, is_active=True)
        ser_data = ArticleSerializer(instance=article)
        return Response(data=ser_data.data, status=status.HTTP_200_OK)
