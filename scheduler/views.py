from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "scheduler/index.html")

def firstYear(request):
    return render(request, "scheduler/firstYear/firstYear.html")

def secondYear(request):
    return render(request, "scheduler/secondYear/secondYear.html")

def thirdYear(request):
    return render(request, "scheduler/thirdYear/thirdYear.html")

def forthYear(request):
    return render(request, "scheduler/forthYear/forthYear.html")