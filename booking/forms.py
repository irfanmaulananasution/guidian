from django import forms
from booking import models

class BookingForm(forms.Form):
    fullName = forms.CharField(
        max_length=50,
        required=True,
        widget = forms.TextInput(attrs = {'placeholder':'Name', 'class' : 'form-control form-control-sm'})
    )

    mail = forms.EmailField(
        max_length=254,
        required=True,
        widget = forms.TextInput(attrs = {'placeholder':'example@mail.com', 'class' : 'form-control form-control-sm'})
    )

    # not finished yet
    participants = forms.IntegerField(
        required=True,
        widget = forms.TextInput(attrs = {'placeholder':'1', 'class' : 'form-control form-control-sm'})
    )

    country = forms.CharField(max_length = 50,
        required=True,
        widget = forms.TextInput(attrs = {'placeholder':'Australia', 'class' : 'form-control form-control-sm'})
    )

    phone = forms.IntegerField(
        required=True,
        widget = forms.TextInput(attrs = {'placeholder':'+62812345678', 'class' : 'form-control form-control-sm'})
    )