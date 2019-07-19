from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
#import the student form
from .forms import HouseForm


def add_house (request):

    #form to input a new student
    form = HouseForm(request.POST or None) 

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save() 

    context = { 
        "form":form
    }

    return render(request, "houses/house.html", context)