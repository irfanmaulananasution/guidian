from django import forms
from regularTour import models

class CreateRegularTourForm(forms.Form):
    destination = forms.CharField(
        label = 'Destination',
        required = True,
        max_length = 15,
        widget = forms.TextInput(attrs={
            'class': 'form-control',
            'type': 'text',
            'placeholder': 'China Town'
        })
    )

    description = forms.CharField(
        label = 'Description',
        required = True,
        max_length = 300,
        widget = forms.Textarea(attrs={
            'class': 'form-control',
            'type': 'text',
            'placeholder': 'Write the description here'
        })
    )

    distance = forms.CharField(
        label = 'Distance',
        required = True,
        max_length = 5,
        widget = forms.TextInput(attrs={
            'class': 'form-control',
            'type': 'text',
            'placeholder': 'Approx. 3 kms'
        })
    )

    duration = forms.CharField(
        label = 'Duration',
        required = True,
        max_length = 10,
        widget = forms.TextInput(attrs={
            'class': 'form-control',
            'type': 'text',
            'placeholder': '2 - 3 hours'
        })
    )

    meeting_point = forms.CharField(
        label = 'Meeting Point',
        required = True,
        max_length = 150,
        widget = forms.TextInput(attrs={
            'class': 'form-control',
            'type': 'text',
            'placeholder': 'In the area of Candra Naya building, Novotel Hotel Gajah Mada. Jl. Gajah Mada No. 188, Jakarta Barat.'
        })
    )

    route = forms.CharField(
        label = 'Route',
        required = True,
        max_length = 100,
        widget = forms.TextInput(attrs={
            'class': 'form-control',
            'type': 'text',
            'placeholder': 'Candra Naya - Pantjoran Tea House - Petak Sembilan - Dharma Bakti Temple - St. Maria de Fatima Church - Toa Se Bio'
        })
    )

    photo = forms.CharField(
        label = 'Photo',
        required = True,
        widget = forms.TextInput(attrs={
            'class': 'form-control',
            'type': 'text',
            'placeholder': 'Upload to imgbb.com then copy the link here'
        })
    )

    location_map = forms.CharField(
        label = 'Location Map',
        required = True,
        widget = forms.TextInput(attrs={
            'class': 'form-control',
            'type': 'text',
            'placeholder': 'Write map location here'
        })
    )

class Meta:
    model = models.RegularTourModel
    fields = (
        'destination',
        'description',
        'distance',
        'duration',
        'meeting_point',
        'route',
        'photo', 
        'location_map'
    )

class UpdateRegularTourForm(forms.Form):
    destination = forms.CharField(
        label = 'Destination',
        required = True,
        widget = forms.TextInput(attrs={
            'class': 'form-control',
            'type': 'text',
            'placeholder': 'China Town'
        })
    )

    description = forms.CharField(
        label = 'Description',
        required = True,
        widget = forms.Textarea(attrs={
            'class': 'form-control',
            'type': 'text',
            'placeholder': 'Write the description here'
        })
    )

    distance = forms.CharField(
        label = 'Distance',
        required = True,
        widget = forms.TextInput(attrs={
            'class': 'form-control',
            'type': 'text',
            'placeholder': 'kms'
        })
    )

    duration = forms.CharField(
        label = 'Duration',
        required = True,
        widget = forms.TextInput(attrs={
            'class': 'form-control',
            'type': 'text',
            'placeholder': 'hours'
        })
    )

    meeting_point = forms.CharField(
        label = 'Meeting Point',
        required = True,
        widget = forms.TextInput(attrs={
            'class': 'form-control',
            'type': 'text',
            'placeholder': 'In the area of Candra Naya building, Novotel Hotel Gajah Mada. Jl. Gajah Mada No. 188, Jakarta Barat.'
        })
    )

    route = forms.CharField(
        label = 'Route',
        required = True,
        widget = forms.TextInput(attrs={
            'class': 'form-control',
            'type': 'text',
            'placeholder': 'Candra Naya - Pantjoran Tea House - Petak Sembilan - Dharma Bakti Temple - St. Maria de Fatima Church - Toa Se Bio'
        })
    )

    # photo = forms.ImageField(
    #     label = 'Photo',
    #     required = True,
    #     help_text = 'Upload photo destination here'
    # )

    photo = forms.CharField(
        label = 'Photo',
        required = True,
        widget = forms.TextInput(attrs={
            'class': 'form-control',
            'type': 'text',
            'placeholder': '.jpg'
        })
    )

    location_map = forms.CharField(
        label = 'Location Map',
        required = True,
        widget = forms.TextInput(attrs={
            'class': 'form-control',
            'type': 'text',
            'placeholder': 'Write map location here'
        })
    )

class Meta:
    model = models.RegularTourModel
    fields = (
        'destination', 
        'description', 
        'distance', 
        'duration', 
        'meeting_point', 
        'route', 
        'photo', 
        'location_map'
    )
