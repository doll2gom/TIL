from django.shortcuts import render, redirect
from .models import Album
from .forms import AlbumForm

# Create your views here.
def index(request):
    albums = Album.objects.all()
    form = AlbumForm()   
    context = {
        'albums':albums,
        'form':form,
    }
    return render(request, 'albums/index.html', context)


def detail(request, pk):
    album = Album.objects.get(pk=pk)
    context = {
        'album':album,
    }
    return render(request, 'albums/detail.html', context)

    
def create(request):
    form = AlbumForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('albums:detail')

def new(request):
    form = AlbumForm()
    context = {
        'form': form,
    }
    return render(request, 'albums/create.html', context)