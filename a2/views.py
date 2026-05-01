from django.shortcuts import render,redirect
from .forms import StudentForm

def new(request):
    form = StudentForm()
    if  request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/students/add")

    return render(request,"new.html",{"form":form})
