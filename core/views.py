from django.shortcuts import render
from rest_framework import generics
from .serializers import CustomUserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework import mixins
from core.models import CustomUser
# Create your views here.
# class RegisterApiView(
#     generics.GenericAPIView
# ):
#     serializer_class = CustomUserSerializer

# #     def post(self, request):
#         serlizer = self.serializer_class(
#             request.data
#         )
#         if serlizer.is_valid():
#             serlizer.save()
#             return Response(
#                 data=serlizer.data,
#                 status=status.HTTP_201_CREATED
#             )
#         return Response(
#             data=serlizer.errors,
#             status=status.HTTP_400_BAD_REQUEST
#         )


class RegisterUserViewSet(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin
):
    serializer_class = CustomUserSerializer
    model = CustomUser