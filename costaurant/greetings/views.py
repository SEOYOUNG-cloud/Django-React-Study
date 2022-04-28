from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h2>정답입니다!</h2>")
