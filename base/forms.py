
from .models import Item
from django import forms


class serverformClass(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['ServerName']


class DateformClass(forms.Form):
    export_to_csv = forms.BooleanField(required=False)
    start_date = forms.DateTimeField(required=False)
    end_date = forms.DateTimeField(required=False)

    class Meta:
        model = Item
        fields = ['export_to_csv', 'start_date', 'end_date']
