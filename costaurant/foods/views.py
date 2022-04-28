from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def index(request):
    today = datetime.today()
    context = {'date' : today}
    return render(request, 'foods/index.html', context=context)
# template을 유저에게 보여준다 = Template을 rander한다
# rander() 함수는 httpResponse를 만들어서 return 해준다.
'''
render 함수는 인자로 주어진 템플릿을 사전형(dict) 인자인 context와 결합해서 렌더링을 거친 다음 
HttpResponse 객체로 반환하는 함수입니다. 
쉽게 말하면 인자로 넘겨주는 템플릿과 context 데이터를 합쳐서 HttpResponse 객체로 돌려주는 함수인 거죠.
필수인자는 request와 template_name
'''

