from re import T
from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from .models import Article, Comments
from .serializers import ArticleSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly
from .pagination import CustomPagination, CustomPaginationLimitOffset, CustomCursosPagination
from rest_framework.decorators import action
from rest_framework.response import Response



class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (IsOwnerOrReadOnly,)
    # pagination_class = CustomPagination

    @action(detail=True, methods=["GET"])
    def get_comments(self, request, pk=None):
        comments = Comments.objects.all().filter(
            article_id=pk
        )
        serialized = CommentSerializer(comments, many=True)
        return Response(serialized.data)