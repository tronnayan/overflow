from django.contrib import admin
from .models import Reply, extUser, Tag, Question, Answers, VoteAnswer, VoteQuestion
# Register your models here.
admin.site.register(extUser)
admin.site.register(Tag)
admin.site.register(Question)
admin.site.register(Answers)
admin.site.register(Reply)
admin.site.register(VoteAnswer)
admin.site.register(VoteQuestion)
