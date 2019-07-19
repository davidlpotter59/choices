from django import forms
from .models import Student
from houses.models import House
from django.forms import ModelChoiceField

class StudentForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput())
    house = forms.ModelChoiceField(queryset=House.objects.all(), initial=0)
    # house = forms.ModelMultipleChoiceField(queryset=House.objects.all())
    class Meta:
        model = Student
        fields = [
                "name",
                "house",
                 ]