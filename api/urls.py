from django.urls import path,include
from api.views import *

urlpatterns = [
     path('register',RegisterView.as_view()),
     path('user',UserView.as_view()),
     path('question',QuestionView.as_view()),
     path('tag',TagView.as_view()),
]