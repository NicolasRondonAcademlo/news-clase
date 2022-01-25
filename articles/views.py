from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from .models import Article
from .serializers import ArticleSerializer
from .permissions import IsOwnerOrReadOnly, IsAuthenticated

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (IsOwnerOrReadOnly)