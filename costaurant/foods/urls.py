from django.contrib import admin
from django.urls import path
from . import views 
# 여기서 . 은 같은 디렉토리 안을 보라는 뜻이다.

urlpatterns = [
    path('index/', views.index) # views.py를 보라는 뜻
    # views 모듈에서 index 함수를 가져오는 것
]
