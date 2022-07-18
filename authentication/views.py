from os import stat
from urllib import response
from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.response import Response
from .models import User
from . import serializers
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class UserAuthView(generics.GenericAPIView):
    @swagger_auto_schema(operation_summary="User auth")
    def get(self,request):
        return Response(data={"message":"Hello user"}, status=status.HTTP_200_OK)


class UserCreateView(generics.GenericAPIView):
    serializer_class=serializers.UserCreationSerializer
    permission_classes=[IsAuthenticated]
    
    @swagger_auto_schema(operation_summary="Create user account")
    def post(self,request):
        data=request.data
        serializer=self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
