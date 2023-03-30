from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Todo
from .forms import MyForm
from .forms import NameForm

# Create your views here.
def index(request):
    todoList = Todo.objects.all()
    return render(request, 'todos/index.html', {'todoList' : todoList})


def detail(request, pk):
    todo = Todo.objects.get(pk=pk)
    return render(request, 'todos/detail.html', {'todo': todo})


def new(request):
    return render(request, 'todos/new.html')

def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    priority = request.GET.get('priority')
    deadline = request.GET.get('deadline')
    todo = Todo(title=title, content=content, priority=priority, deadline=deadline )
    todo.save()
    return render(request, 'todos/create.html')

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('todos/create.html')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'todos/form.html', {'form': form})