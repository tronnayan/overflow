from django.db.models import Count
from django.http import request
from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from django.db.models import Q
from api.models import Answers, Question, Tag, VoteAnswer, VoteQuestion
from .serializers import AnswerSerializer, QuestionSerializer, RegisterSerializer, ReplySerializer, TagSerializer, UserSerializer, VoteAnswerSerializer, VoteQuestionSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
import datetime
# Create your views here.

class DashboardView(APIView):
    def get(self, request):
        questions = Question.objects.annotate(votes = Count('ques_votes'))
        serializer = QuestionSerializer(questions.order_by('votes').reverse()[:5], many = True)
        return Response(serializer.data)

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
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many = True)
        return Response(serializer.data)

    def post(self, request):
        user = User.objects.get(id = request.user.id)
        dt = datetime.datetime.now()
        res = request.data 
        res['user'] = user.id
        res['updatedat'] = dt
        serializer = QuestionSerializer(data = res)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class AnswerView(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        user = User.objects.get(id = request.user.id)
        dt = datetime.datetime.now()
        res = request.data 
        res['user'] = user.id
        res['updatedat'] = dt
        serializer = AnswerSerializer(data = res) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class TagView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        tags  = Tag.objects.all()
        serializer = TagSerializer(tags, many = True)
        return Response(serializer.data)

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

class ReplyView(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        user = User.objects.get(id = request.user.id)
        dt = datetime.datetime.now()
        data = {
            "user" : user.id,
            "reply" : request.data.get("reply"),
            "answer" : request.data.get("answer"),
            "updatedat" : dt
        }
        serializer = ReplySerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class VoteQuestionView(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        user = User.objects.get(id = request.user.id)
        if VoteQuestion.objects.filter(Q(user = user) & Q(question_id = request.data.get("question"))).exists():
            return Response("You have voted for this Question")
        data = {
            "user" : user.id,
            "question" : request.data.get("question")
        } 
        serializer = VoteQuestionSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def delete(self, request):
        user = User.objects.get(id = request.user.id)
        vote_obj = VoteQuestion.objects.get(Q(user = user) & Q(question_id = request.data.get("question"))).delete()
        return Response({"Down voted for Question"})


class VoteAnswerView(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        user = User.objects.get(id = request.user.id)
        if VoteAnswer.objects.filter(Q(user = user) & Q(answer_id = request.data.get("answer"))).exists():
            return Response("You have voted for this Answer")
        data = {
            "user" : user.id,
            "answer" : request.data.get("answer")
        } 
        serializer = VoteAnswerSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def delete(self, request):
        user = User.objects.get(id = request.user.id)
        vote_obj = VoteAnswer.objects.get(Q(user = user) & Q(answer_id = request.data.get("answer"))).delete()
        return Response({"Down voted for an Answer"})

class TagSearchView(APIView):
    def get(self, request):
        obj = Tag.objects.filter(tag_name__icontains = request.data.get("query"))
        serializer = TagSerializer(obj,many = True)
        return Response(serializer.data)

class QuestionSearchByTagView(APIView):
    def get(self,request,tag_id):
        tag = Tag.objects.get(id = tag_id)
        questions = tag.questions.all()
        serializer = QuestionSerializer(questions,many = True)
        return Response(serializer.data)

class SearchQuestionView(APIView):
    def get (self, request):
        text = request.data.get("query")
        questions = Question.objects.filter(Q(question__icontains = text) | Q(title__icontains = text))
        serializer = QuestionSerializer(questions, many = True)
        return Response(serializer.data)

class SearchAnswerView(APIView):
    def get (self, request):
        text = request.data.get("query")
        answers = Answers.objects.filter(answer__icontains = text)
        serializer = AnswerSerializer(answers, many = True)
        return Response(serializer.data)