# weight/forms.py

from django import forms
from .models import WeightRecord

class WeightRecordForm(forms.ModelForm):
    class Meta:
        model = WeightRecord
        fields = ['weight']

    def clean_weight(self):
        weight = self.cleaned_data.get('weight')
        if weight <= 0:
            raise forms.ValidationError("Weight must be a positive number.")
        return weight
    

class DateRangeForm(forms.Form):
    start_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
