from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, Post Pandemic World. You are in PERSONNA CHALLENGE.")