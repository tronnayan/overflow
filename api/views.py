from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from .serializers import RegisterSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class UserView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        user = User.objects.get(id = request.user.id)
        serializer = UserSerializer(user, many = False)
        return Response(serializer.data)
    
    def put(self,request):
       user  = User.objects.get(id = request.user.id)
       data = {
           "username" : request.data.get("username"),
           "email" : request.data.get("email")
       }
       serializer = UserSerializer(instance = user, data = data, partial = True)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)

