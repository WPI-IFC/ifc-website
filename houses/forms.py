from django import forms

from .models import Fraternity

class HouseForm(forms.ModelForm):

    class Meta:
        model = Fraternity
        fields = '__all__'
