from django.shortcuts import render,redirect
from .models import Todo
from .forms import TodoForm

# Create your views here.
def index(request):
    todos = Todo.objects.all()
    print(todos)
    context = {
        'todos':todos
    }
    return render(request, 'todos/index.html', context)

def detail(request, pk):
    todo = Todo.objects.get(pk=pk)
    context = {
        'todo':todo,
    }
    return render(request, 'todos/detail.html', context)


def create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save()
            return redirect('todos:detail', todo.pk)
    else:
        form = TodoForm()
    context = {
        'form': form,
    }
    return render(request, 'todos/new.html', context)

def delete(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()
    return redirect('todos:index')


def update(request, pk):
    todo = Todo.objects.get(pk=pk)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid(): 
            form.save()
            return redirect('todos:detail', todo.pk)
    else:
        form = TodoForm()
    context = {
        'todo':todo,
        'form': form,
    }
    return render(request, 'todos/edit.html', context)