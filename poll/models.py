from django.db import models
from django.utils import timezone
import datetime
# Create your models here.

class Question(models.Model):
    question_content = models.CharField(max_length=200)
    question_published_date = models.DateTimeField("published date")
    
    def __str__(self):
        return self.question_content
    def was_published_recently(self):
        return self.question_published_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    choice_question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_content = models.CharField(max_length=200)
    choice_tally = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_content