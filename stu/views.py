from django.shortcuts import render
from .models import Stu
def home(request):
    # d = Stu.objects.filter(name="sam")
    d = Stu.objects.all()
    return render(request,"home.html",{"data":d})

def studentDetail(request,pk):
    d = Stu.objects.filter(pk=pk)
    return render(request,"home.html",{"data":d})
    