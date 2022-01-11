from django.urls import path,include
from api.views import *

urlpatterns = [
     path('register',RegisterView.as_view()),
     path('user',UserView.as_view()),
]