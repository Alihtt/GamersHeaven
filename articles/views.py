from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import ArticleSerializer
from .models import Article
from .paginations import StandardResultsSetPagination
from .mixins import MultipleFieldLookupMixin
from permissions import IsOwnerOrReadOnly


class ArticleListCreate(ListCreateAPIView):
    queryset = Article.objects.filter(is_active=True).all()
    serializer_class = ArticleSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [IsOwnerOrReadOnly]


class ArticleDetail(MultipleFieldLookupMixin, RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.filter(is_active=True).all()
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ArticleSerializer
    lookup_fields = ['pk', 'slug']
