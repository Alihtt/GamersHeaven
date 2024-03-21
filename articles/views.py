from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from .serializers import ArticleSerializer, CategorySerializer
from .models import Article, Category
from .paginations import StandardResultsSetPagination
from .mixins import MultipleFieldLookupMixin
from permissions import IsOwnerOrReadOnly


class ArticleListCreate(ListCreateAPIView):
    """
    GET -> List of Articles

    POST -> Create Article
    """

    queryset = Article.objects.filter(is_active=True).all()
    serializer_class = ArticleSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [IsOwnerOrReadOnly]


class ArticleDetail(MultipleFieldLookupMixin, RetrieveUpdateDestroyAPIView):
    """
    GET -> Article detail

    PUT -> update Article

    PATCH -> partial update Article

    DELETE -> delete Article
    """

    queryset = Article.objects.filter(is_active=True).all()
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ArticleSerializer
    lookup_fields = ['pk', 'slug']


class CategoryList(ListAPIView):
    """
        GET -> List of main categories
    """

    queryset = Category.objects.filter(is_sub=False, is_active=True)
    serializer_class = CategorySerializer
