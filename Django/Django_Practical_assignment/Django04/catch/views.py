from django.shortcuts import render

# Create your views here.
def catch(request):
    data = request.GET.get('content')
    context = {
        'data':data
    }
    return render(request, 'catch/catch.html', context)