from django.template import loader
from django.http import Http404, HttpResponse
from .models import Question
from django.shortcuts import render, get_object_or_404

# Create your views here.

#This returns 'Hello World'
# def index(request):
#     return HttpResponse("Hello World!")

#This returns the QUESTION (Hard coded)
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     output = ', '.join([q.question_text for q in latest_question_list])
#     return HttpResponse(output)

#This returns the question from templates
def index2(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:7]
    template = loader.get_template('polls/index.html')
    context = {'latest_question_list': latest_question_list,}
    return HttpResponse(template.render(context, request))

#This returns the question from templates using render shortcut
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

#     response declared directly
# def detail(requst, question_id):
#     return HttpResponse("You're looking at questions %s." % question_id)
     
    #response from variable
# def detail(requst, question_id):
#     response = "You're looking at questions %s from new format."
#     return HttpResponse(response % question_id)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(requst, question_id):
    response = "You're looking at the result of the question %s."
    return  HttpResponse(response % question_id)

def vote(requst, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def error_page(request, question_id):
    try:    
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/error_page.html', {'question': question})

