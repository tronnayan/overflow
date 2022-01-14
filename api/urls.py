from django.urls import path,include
from api.models import VoteQuestion
from api.views import *

urlpatterns = [
     path('register',RegisterView.as_view()),
     path('user',UserView.as_view()),
     path('question',QuestionView.as_view()),
     path('answer',AnswerView.as_view()),
     path('tag',TagView.as_view()),
     path('search-tag', TagSearchView.as_view()),
     path('view-questions/<int:tag_id>', QuestionSearchByTagView.as_view()),
     path('reply',ReplyView.as_view()),
     path('vote-question',VoteQuestionView.as_view()),
     path('vote-answer',VoteAnswerView.as_view()),
     path('search-questions',SearchQuestionView.as_view()),
     path('search-answers',SearchAnswerView.as_view()),
]