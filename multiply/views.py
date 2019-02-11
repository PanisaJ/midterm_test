from django.shortcuts import HttpResponse, render
from django.template import loader

def mulitiplication(request):
    if request.POST.get('num'):
        number = int(request.POST.get('num'))
        results = []
        for i in range(1,13):
            if(i==1):
                 results.append(number)
            else:
                 result = results[i-2]+number
                 results.append(result)
        return render(request,'multiply/multiTable.html',{'results' : results,'number':number,})
    else:
        return render(request,'multiply/index.html',{'error_message': "You didn't insert input."})

def index(request):
    return render(request,'multiply/index.html')
