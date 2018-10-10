from django.forms.widgets import TextInput


class Html5Date(TextInput):
    input_type = "date"


class Html5Time(TextInput):
    input_type = "time"