from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.fields import TextField
from django.db.models.fields.files import FileField
# Create your models here.

# Create your models here.
class extUser(models.Model):  
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name="extuser")
    bio = models.TextField(blank = True)
    profile_img = models.ImageField(null = True, blank = True)
    def __str__(self):
        return self.user.username

class Tag(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tag_name = models.CharField(max_length=50, unique=True, blank=True)
    createdat = models.DateTimeField(auto_now=True,null=True)
    updatedat = models.DateTimeField(auto_now=False,null=True)

class Question(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.TextField(blank=True)
    question = models.TextField(blank=True)
    attachments = models.FileField(null=True)
    tags = models.ManyToManyField(Tag, blank=True,related_name = "questions")
    createdat = models.DateTimeField(auto_now=True,null=True)
    updatedat = models.DateTimeField(auto_now=False,null=True)
    
class VoteQuestion(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE,  related_name="ques_votes")

class Answers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers")
    answer = TextField()
    attachments= models.FileField(null=True)
    createdat = models.DateTimeField(auto_now=True,null=True)
    updatedat = models.DateTimeField(auto_now=False,null=True)


class VoteAnswer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    answer = models.ForeignKey(Answers, on_delete=models.CASCADE, null=True, related_name="ans_votes")


class Reply(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    reply = models.TextField()
    answer = models.ForeignKey(Answers,on_delete=models.CASCADE, related_name="replies")
    createdat = models.DateTimeField(auto_now=True,null=True)
    updatedat = models.DateTimeField(auto_now=False,null=True)



