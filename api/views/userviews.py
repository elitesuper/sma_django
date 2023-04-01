from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.decorators import api_view

from ..serializers.users import UserSerializer, UserLoginSerializer
# Create your views here.
@api_view(['GET', 'OPTIONS', 'POST'])
def user_register(request):
    serializer = UserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    token, created = Token.objects.get_or_create(user=user)
    return Response({'token': token.key})

    

@api_view(['GET','OPTIONS', 'POST'])
def user_login(request):
    serializer = UserLoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data
    token, created = Token.objects.get_or_create(user=user)
    return Response({'token': token.key})