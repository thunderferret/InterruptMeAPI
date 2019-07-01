from django.shortcuts import render
from django.urls import resolve
from django.http import Http404, HttpResponse

# Create your views here.

def user_settings(request, uuid):
    return HttpResponse("This is a reponse for user_setting")