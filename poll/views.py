from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Question, Choice
# Create your views here.

class IndexView(generic.ListView):
    template_name = 'poll/index.html'
    context_object_name = 'questions'

    def get_queryset(self):
        return Question.objects.order_by('-question_published_date')[:5]

class DetailView(generic.DetailView):
    template_name = 'poll/detail.html'
    model = Question

class ResultsView(generic.DetailView):
    template_name = 'poll/results.html'
    model = Question


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

class ResultsView(generic.DetailView):
    template_name = 'poll/results.html'
    model = Question