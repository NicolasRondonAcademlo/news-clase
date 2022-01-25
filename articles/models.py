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