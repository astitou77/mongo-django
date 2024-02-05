from django.shortcuts import render

# ADDED
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello World of Python App Monitors !!!")
