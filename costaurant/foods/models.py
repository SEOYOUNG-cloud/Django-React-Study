from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    price = models.IntegerField()
    img_path = models.CharField(max_length=255)
    
    def __str__(self): # 이 Menu 클래스를 하나의 문자열로 표현해주는 함수
        return self.name
        # print(Menu)를 썼을 때 결과로 나오는 문자열을 넣어줌