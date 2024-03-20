from rest_framework.generics import ListAPIView
from articles.serializers import ArticleSerializer
from articles.paginations import StandardResultsSetPagination
from articles.models import Article


class HomeArticlesList(ListAPIView):
    """
    List of Articles
    """

    queryset = Article.objects.filter(is_active=True).all()
    serializer_class = ArticleSerializer
    pagination_class = StandardResultsSetPagination
