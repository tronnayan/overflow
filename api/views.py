from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions
from rest_framework.serializers import Serializer
from rest_framework.views import APIView

from api.models import Question
from .serializers import QuestionSerializer, RegisterSerializer, TagSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
import datetime
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

class QuestionView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request):
        questions = Question.objects.filter(user = request.user)
        serializer = QuestionSerializer(questions, many = True)
        return Response(serializer.data)

    def post(self, request):
        user = User.objects.get(id = request.user.id)
        data = {
            "user" : user.id,
            "title" : request.data.get("title"),
            "tags" : request.data.get("tags"),
            "question":request.data.get("question")
        }
        serializer = QuestionSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class TagView(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        user = User.objects.get(id = request.user.id)
        dt = datetime.datetime.now()
        data = {
            "user" : user.id,
            "tag_name" : request.data.get("tag_name"),
            "updatedat" : dt
        }
        serializer = TagSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)