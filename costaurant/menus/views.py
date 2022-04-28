from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def index(request):
    today = str(datetime.now().date()) # 오늘 날짜 가져오기
    context = {'date' : today}
    return render(request, 'menus/index.html', context = context)