from pyexpat import model
from rest_framework import serializers
from .models import Article, Comments


class CommentSerializer(
    serializers.ModelSerializer
):
    class Meta:
        model = Comments
        fields = ('id','body')


class ArticleSerializer(
    serializers.ModelSerializer
):
    class Meta:
        model= Article
        fields = ('__all__')

