from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello World!")

def detail(requst, question_id):
    return HttpResponse("You're looking at questions %s." % question_id)

def results(requst, question_id):
    response = "You're looking at the result of the question %s."
    return  HttpResponse(response % question_id)

def vote(requst, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

