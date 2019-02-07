from django.shortcuts import renderf
from django.http import HttpResponse
# Create your views here.

def detail(request, question_id):
    return HttpResponse("you are looking at question %s" % question_id)

def results(request, question_id):
    response = "you are looking at the result of question %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)