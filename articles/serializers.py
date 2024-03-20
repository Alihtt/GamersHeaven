from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    url = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = '__all__'

    def get_url(self, obj):
        return obj.get_absolute_url()

    def validate_author(self, data):
        if data == self.context['request'].user:
            return data
        raise serializers.ValidationError('You must add your id')
