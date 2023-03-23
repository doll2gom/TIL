from django.shortcuts import render

# Create your views here.
def calculate(request, number1, number2):
    context = {
        'plus' : number1 + number2,
        'min' : number1 - number2,
        'mult' : number1 * number2,
        'shr' : number1 // number2
    }
    return render(request, 'calculate/calculate.html', context)