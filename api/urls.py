from django.urls import path,include
from api import views
urlpatterns = [
     path('register',views.RegisterView.as_view())
]