from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
#import template loader
from django.template import loader
from .models import Question
#import error template for custom error messages
from django.http import Http404

# Create your views here.

# def index(request):
#     return HttpResponse('Hello world')

# method 1 of rendering a template
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     (loader function is imported and needed only if you are using loader.get_template)
#     template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list
#     }
#     return HttpResponse(template.render(context,request))
#method 2 of rendering a template
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list
        }
    return render(request, 'polls/index.html', context)

#Basic detail view
# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)

#Detail view with error message
# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'polls/detail.html', {'question': question})


#Detail view with error message 2
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
