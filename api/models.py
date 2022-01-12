from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.fields import TextField
from django.db.models.fields.files import FileField
# Create your models here.

# Create your models here.
class extUser(models.Model):  
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.TextField(blank = True)
    def __str__(self):
        return self.user.username

class Tag(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tag_name = models.CharField(max_length=50, blank=True)
    createdat = models.DateTimeField(auto_now=True,null=True)
    updatedat = models.DateTimeField(auto_now=False,null=True)

class Question(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.TextField(blank=True)
    question = models.TextField(blank=True)
    tags = models.ForeignKey(Tag,on_delete=models.CASCADE)
    vote_count = models.IntegerField(default = 0)
    createdat = models.DateTimeField(auto_now=True,null=True)
    updatedat = models.DateTimeField(auto_now=False,null=True)
    
class VoteQuestion(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

class VoteAnswer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

class Answers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = TextField()
    attachments= models.FileField(upload_to='answer_attachments/', null=True)
    reply = models.ForeignKey("self",on_delete=models.CASCADE)
    vote_count = models.IntegerField(default = 0)
    createdat = models.DateTimeField(auto_now=True,null=True)
    updatedat = models.DateTimeField(auto_now=False,null=True)





