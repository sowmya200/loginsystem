from django.shortcuts import render
from django.http import HttpResponse
#from rest_framework.response import Response


def home(request):
    return HttpResponse("hello i am working")


