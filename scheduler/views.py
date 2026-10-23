from django.shortcuts import render
from .models import Section

# Create your views here.
def index(request):
    return render(request, "scheduler/index.html", {
        "sections": Section.objects.all(),
    })

def firstYear(request):
    return render(request, "scheduler/firstYear/firstYear.html")

def secondYear(request):
    return render(request, "scheduler/secondYear/secondYear.html")

def thirdYear(request):
    return render(request, "scheduler/thirdYear/thirdYear.html")

def forthYear(request):
    return render(request, "scheduler/forthYear/forthYear.html")