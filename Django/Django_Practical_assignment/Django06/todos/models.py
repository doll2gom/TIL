from django.db import models

# Create your models here.
class Todo(models.Model):
    content = models.CharField(max_length=80)
    completed = models.BooleanField(default=False)
    priority = models.IntegerField(default=3)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True)

"""
1. 아래 할 일 생성
content : 실습 제출
priority : 5
completed : False
deadline : 오늘 날짜(년-월-일)
"""
from todos.models import Todo
todo = Todo()
todo.content = '실습 제출'
todo.priority = 5
todo.completed = False
from datetime import datetime
todo.deadline = datetime(2023,3,28)

todo.save()
Todo.objects.all()


"""
2. 아래 할 일 생성
content : 데일리 설문(오후) 제출
deadline : 오늘 날짜(년-월-일)
"""
todo = Todo(content='데일리 설문(오후) 제출', deadline=datetime(2023,3,28))
todo.save()


"""
3. 임의의 할 일 5개 생성
"""
Todo.objects.create(content='깃허브 TIL 정리')
Todo.objects.create(content='파이썬 클래스 강의 다시듣기')
Todo.objects.create(content='그리드 이해')
Todo.objects.create(content='데일리 알고리즘 문제 풀기')
Todo.objects.create(content='햇님반 스터디 모임 참석')


"""
4. pk 기준 오름차순으로 정렬한 모든 데이터 조회
"""
Todo.objects.order_by('pk')


"""
5. priority 기준 내림차순으로 정렬한 모든 데이터 조회
"""
Todo.objects.order_by('-priority')


"""
6. pk가 1인 단일 데이터의 아래 필드 조회
(pk, content, priority, deadline, created_at)
"""
Todo.objects.get(pk=1)
