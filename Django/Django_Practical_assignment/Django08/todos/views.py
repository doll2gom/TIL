from django.shortcuts import render, redirect
from .models import Todo
# Create your views here.
def index(request):
    todo = Todo.objects.all()
    context = {
        'todos':todo
    }
    # 페이지(데이터)를 그냥 불러올 때 사용
    return render(request, 'todos/index.html', context)

def detail(request, pk):
    # 어떤 내용을 삭제할지 정보가 필요하기 때문에 pk값은 필요하다
    todo = Todo.objects.get(pk=pk)
    context = {
        'todo':todo
    }
    return render(request, 'todos/detail.html', context)

def new(request):
    return render(request, 'todos/new.html')

def create(request):
    # 조회 
    # new 입력한 데이터를 변수에 할당
    title = request.POST.get('title')
    content = request.POST.get('content')
    priority = request.POST.get('priority')
    completed = request.POST.get('completed')
    deadline = request.POST.get('deadline')

    # DB에 생성+저장 
    todo = Todo(title=title, content=content, priority=priority, deadline=deadline, completed=completed) == 'on'
    todo.save()
    
    # 이동할 주소로(url)을 반환한다.
    # 페이지로 이동할 수 있도록 도와준다.
    return redirect('todos:detail', todo.pk)

def delete(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()
    return redirect('todos:index')

def edit(request, pk):
    # 수정할 데이터 조회
    todo = Todo.objects.get(pk=pk)
    context = {
        'todo':todo
    }
    return render(request, 'todos/edit.html', context)

def update(request, pk):
    # 조회 delete
    todo = Todo.objects.get(pk=pk)    
    # 수정1 # 변수에 할당 데이터 create
    title = request.POST.get('title')
    content = request.POST.get('content')
    priority = request.POST.get('priority')
    deadline = request.POST.get('deadline')
    completed = request.POST.get('completed') == 'on'
    # 수정2 # 변수값 변경
    todo.title = title
    todo.content = content
    todo.priority = priority
    todo.deadline = deadline
    todo.completed = completed
    # 저장 create
    todo.save()
    return redirect('todos:detail', todo.pk)