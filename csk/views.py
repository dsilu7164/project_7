from django.shortcuts import render
from django.http import  HttpResponse
# Create your views here.
def msd(request):
    return render(request,'msd.html')
def jadu(request):
    return HttpResponse('best allrounder')