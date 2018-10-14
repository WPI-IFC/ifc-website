from django import forms
import re

from .models import Fraternity

class HouseForm(forms.ModelForm):

    class Meta:
        model = Fraternity
        fields = '__all__'

    def clean_calendar_link(self):
        data = self.cleaned_data['calendar_link']
        if not re.match("^https://calendar.google.com/calendar/embed\?src=(.*)", data):
            raise forms.ValidationError("Link provided is not a google calendar link!")
        
        return data