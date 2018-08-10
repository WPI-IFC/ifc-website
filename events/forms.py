from django import forms

from .models import OfficerEvent, HouseEvent


class OfficerEventForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(OfficerEventForm, self).__init__(*args, **kwargs)
        self.fields["splash_img"].label = "Splash Image"
        self.fields["date"].label = "Date"
        self.fields["start_time"].label = "Start Time"
        self.fields["end_time"].label = "End Time"

    class Meta:
        model = OfficerEvent
        fields = ("title", "description", "date", "start_time", "end_time", "splash_img")


class HouseEventForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(HouseEventForm, self).__init__(*args, **kwargs)
        self.fields["splash_img"].label = "Splash Image"
        self.fields["date"].label = "Date"
        self.fields["start_time"].label = "Start Time"
        self.fields["end_time"].label = "End Time"

    class Meta:
        model = HouseEvent
        fields = ("title", "description", "date", "start_time", "end_time", "splash_img")
