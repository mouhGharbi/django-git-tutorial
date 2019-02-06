from django.db import models

# Create your models here.

class Question(models.Model):
    question_content = models.CharField(max_length=200)
    question_published_date = models.DateTimeField("published date")


class Choice(models.Model):
    choice_question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_content = models.CharField(max_length=200)
    choice_tally = models.IntegerField(default=0)