from django.shortcuts import HttpResponse, render
from django.template import loader

def mulitiplication(request):
    if request.POST.get('num'):
        number = request.POST.get('num')
        results = []
        for r in range(int(number)):
            results.append(number)
        return render(request,'multiply/multiTable.html',{'results' : results})
    else:
        return render(request,'multiply/index.html',{'error_message': "You didn't insert input."})

def index(request):
    return render(request,'multiply/index.html')
