from django.shortcuts import render

# Create your views here.
#import the student form
from .forms import StudentForm


def add_student (request):

    #form to input a new student
    form = StudentForm(request.POST or None) 

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save() 

    context = { 
        "form":form
    }

    return render(request, "student/student.html", context)