from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate,login
from rest_framework import viewsets, status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response  import Response
from rest_framework.authtoken.models import Token


from .models import User
from .serializers import UserSerializer

# Create your views here.

class UserViewSet(viewsets.ViewSet):

    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def user_view(self, request, **kwargs):
        users = User.objects.all()
        serializer = self.serializer_class(users, many=True)

        return Response(serializer.data)
    
    def user_detail(self, request, **kwargs):
        user = User.objects.get(id=kwargs.get('user_id'))
        serializer = self.serializer_class(user)
        return Response(serializer.data, status=200)

    def user_create(self, request, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=400)

    def user_login(self, request, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            # login(request,user)
            token = Token.objects.get(user=user)
            print('token', token.key)
            return Response(token.key, status=200)
        return Response(status=400)
