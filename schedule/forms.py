from django import forms
from .models import RegTourScheduleModel
from daftarGuide.models import GuideModel

class CreateScheduleForm(forms.Form):
    date = forms.DateField(
        required=True,
        widget = forms.DateInput(attrs = {
                'type' : 'date', 
                'class' : 'form-control form-control-sm'
            })
    )

    startTime = forms.TimeField(
        label="Start Time",
        required=True,
        widget = forms.TimeInput(attrs = {
                'type' : 'time', 
                'class' : 'form-control form-control-sm'
            })
    )
    
    slot = forms.IntegerField(
        max_value=20,
        min_value=0,
        required=True,
        widget = forms.NumberInput(attrs = {
                'placeholder':'20', 
                'type' : 'number', 
                'class' : 'form-control form-control-sm'
            })
    )
    
    language = forms.CharField(
        max_length=50, 
        required=True,
        widget = forms.TextInput(attrs = {
                'placeholder':'Language', 
                'class' : 'form-control form-control-sm'
            })
    )

    tourGuide = forms.ModelChoiceField(
        label = "Tour Guide",
        queryset = None, 
        required = False,
        widget = forms.Select(attrs = {
                'class' : 'form-control form-control-sm'
            })
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tourGuide'].queryset = GuideModel.objects.all()

class UpdateScheduleForm(CreateScheduleForm):
    date = forms.DateField(
        widget = forms.DateInput(attrs = {
                'readonly' : True,
                'type' : 'date', 
                'class' : 'form-control form-control-sm'
            })
    )