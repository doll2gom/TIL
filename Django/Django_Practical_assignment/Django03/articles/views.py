from django.shortcuts import render
import random

# Create your views here.
def today_dinner(request):
    foods = ['김밥', '짜장면', '대패삼겹살',]
    context = {
        'foods': random.choice(foods), 
    }
    return render(request, 'articles/today_dinner.html', context)

def throw(request):
    return render(request, 'articles/throw.html')

def catch(request):
    data = request.GET.get('message')
    context = {
        'data': data,
    }
    return render(request, 'articles/catch.html', context)

def lotto_create(request):
    return render(request, 'articles/lotto_create.html')

def lotto(request):
    data = request.GET.get('message')
    output = []
    for i in range(int(data)):
        output.append(random.sample(range(1, 46), 6))
    context = {
        'data': output
    }
    return render(request, 'articles/lotto.html', context)