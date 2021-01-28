import datetime

from django.db import models
from django.utils import timezone

# 데이터의 각 필드는 Field 클래스의 인스턴스로 표현한다.
# DB에선 아래 인스턴스의 이름이 데이터베이스 컬럼명이 된다.

class Question(models.Model):
    question_text = models.CharField(max_length=200) # CharField는 필수 인수가 존재한다.
    pub_date = models.DateTimeField('date published') # 별도의 이름 정의 가능
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) 
    # 각각의 Choice가 하나의 Question에 관계된다는 것을 Django에게 알려준다.
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0) # 선택적인 인수를 가진 Field도 존재한다.

    def __str__(self):
        return self.choice_text