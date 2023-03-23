from django.shortcuts import render

# Create your views here.
def calculate_main(request):
    return render(request, 'calculate_main.html')