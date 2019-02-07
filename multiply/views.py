from django.shortcuts import HttpResponse, render
from django.template import loader

def mulitiplication(request):
    if request.POST.get('number'):
        number = request.POST.get('number')
        a = ""
        for r in range(number):
            a = a + " " + str(number)
        return HttpResponse(a)

def index(request):
    return render(request,'multiply/index.html')
