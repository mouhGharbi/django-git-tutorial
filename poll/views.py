from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice
# Create your views here.

def index(request):
    questions = Question.objects.order_by('-question_published_date')[:5]
    
    return render(request, 'poll/index.html', {'questions': questions})
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'poll/detail.html', {'question':question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'poll/detail.html', {'question':question, 'error_message': "you did not select any choice"})
    else:
        choice.choice_tally += 1
        choice.save()
        return HttpResponseRedirect(reverse('poll:results', args=(question.id,)))


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'poll/results.html', {'question': question})
