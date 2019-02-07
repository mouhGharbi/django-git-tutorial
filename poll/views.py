from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Question
# Create your views here.

def index(request):
    questions = Question.objects.order_by('-question_published_date')[:5]
    
    return render(request, 'poll/index.html', {'questions': questions})
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("the question you asked for does not exist please check the url")
    return HttpResponse("you are looking at question %s" % question_id)

def results(request, question_id):
    response = "you are looking at the result of question %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)