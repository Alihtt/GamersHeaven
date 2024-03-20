from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)
    author = serializers.StringRelatedField(read_only=True)
    category = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Article
        fields = '__all__'

    def get_url(self, obj):
        return obj.get_absolute_url()

    def create(self, validated_data):
        author = self.context['request'].user
        if author.is_staff:
            article = Article(author=author, **validated_data)
            article.save()
            return article
        raise serializers.ValidationError({'message': 'You must be staff'})
