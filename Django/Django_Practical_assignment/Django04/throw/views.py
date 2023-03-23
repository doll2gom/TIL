from django.shortcuts import render

# Create your views here.
def throw(request):
    return render(request, 'throw/throw.html')