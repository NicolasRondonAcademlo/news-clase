from statistics import mode
from turtle import ondrag
from django.db import models
from core.models import CustomUser
# Create your models here.
class Article(models.Model):
    title = models.CharField(
        max_length=150
    )
    body = models.TextField()
    auhtor = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return self.title

class Comments(models.Model):
    author = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE
    )
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE
    )
    body = models.TextField()


