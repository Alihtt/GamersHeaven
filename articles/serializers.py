from rest_framework import serializers
from .models import Article, Category
from drf_spectacular.utils import extend_schema_field
from drf_spectacular.types import OpenApiTypes


class BaseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        serializer_related_field = serializers.StringRelatedField()
        model = Category
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    sub_categories = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = '__all__'

    def get_sub_categories(self, obj):
        categories = obj.categories.all()
        return BaseCategorySerializer(categories, many=True).data


class ArticleSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)
    author = serializers.StringRelatedField(read_only=True)
    category = BaseCategorySerializer

    class Meta:
        model = Article
        fields = '__all__'

    @extend_schema_field(OpenApiTypes.STR)
    def get_url(self, obj):
        return obj.get_absolute_url()

    def create(self, validated_data):
        author = self.context['request'].user
        if author.is_staff:
            article = Article(author=author, **validated_data)
            article.save()
            return article
        raise serializers.ValidationError({'message': 'You must be staff'})
