from django import forms
from .models import House
from django.forms import ModelChoiceField

class HouseForm(forms.ModelForm):
    house_name = forms.CharField(widget=forms.TextInput())
 
    class Meta:
        model = House
        fields = [
                "house_name",
                 ]