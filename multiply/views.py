from django.shortcuts import HttpResponse, render
from django.template import loader
from .models import Statistic

def mulitiplication(request):
    if request.POST.get('num'):
        number = int(request.POST.get('num'))
        try:
             Statistic.objects.get(number=number)
        except:
             print("nooo")
             added_number = Statistic(number=number,times=1)
             added_number.save()
        else:
             print("yesss")
             get_number = Statistic.objects.get(number=number)
             get_number.times += 1
             get_number.save()
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

def history(request):
    return render(request,'multiply/history.html')
