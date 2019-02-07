from django.shortcuts import HttpResponse, render
from django.template import loader

def mulitiplication(request, number):
    
    return render(request,'multiply/multiTable.html',{'number' : number})

