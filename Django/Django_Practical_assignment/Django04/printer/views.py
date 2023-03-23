from django.shortcuts import render

# Create your views here.
def number_print(request, num):
    context = {
        'number': num
    }
    return render(request, 'printer/number_print.html', context)