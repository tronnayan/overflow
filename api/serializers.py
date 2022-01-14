from asyncore import read
from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from .models import Answers, Question, Reply, Tag, VoteAnswer, VoteQuestion

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True,validators=[UniqueValidator(queryset=User.objects.all(), message  = "Email already registered.")])
    class Meta:
        model = User
        fields = ('id','username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create(
        username=validated_data['username'],
        email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
            
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ('id','username', 'email')


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag 
        fields = ('id','user','updatedat','tag_name')

class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = ('id','user','reply','answer','createdat','updatedat')


class VoteAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = VoteAnswer    
        fields = ('user','answer')

class AnswerSerializer(serializers.ModelSerializer):
    replies = ReplySerializer(read_only = True, many = True)
    ans_votes = serializers.SerializerMethodField()

    class Meta:
        model = Answers
        fields = ('id','user','question','answer','createdat','updatedat','replies','ans_votes','attachments')
    
    def get_ans_votes(self, answer):
        return VoteAnswer.objects.filter(answer = answer).count()

class VoteQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = VoteQuestion    
        fields = ('user','question')

class QuestionSerializer(serializers.ModelSerializer):
    # tags = TagSerializer(read_only = True, many = True)
    answers = AnswerSerializer(read_only = True, many = True)
    ques_votes = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = ('id','user','title','question','tags','ques_votes','createdat','updatedat','answers','attachments')
    
    def get_ques_votes(self,question):
        return VoteQuestion.objects.filter(question = question).count()

