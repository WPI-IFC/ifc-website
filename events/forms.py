from django import forms

from .models import OfficerEvent, HouseEvent


class OfficerEventForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(OfficerEventForm, self).__init__(*args, **kwargs)
        self.fields["splash_img"].label = "Splash Image"
        self.fields["d_time"].label = "Date & Time"

    class Meta:
        model = OfficerEvent
        fields = ("title", "description", "d_time", "splash_img")


class HouseEventForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(HouseEventForm, self).__init__(*args, **kwargs)
        self.fields["splash_img"].label = "Splash Image"
        self.fields["d_time"].label = "Date & Time"

    class Meta:
        model = HouseEvent
        fields = ("title", "description", "d_time", "splash_img")