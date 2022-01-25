from logging.handlers import RotatingFileHandler
from posixpath import basename
from django.template import base
from django. urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import RegisterUserViewSet
from articles.views import ArticleViewSet

router = DefaultRouter()
router.register(
    'v1/core/register', RegisterUserViewSet, basename='register'
)
router.register(
    'v1/articles', ArticleViewSet, basename='articulos'
)