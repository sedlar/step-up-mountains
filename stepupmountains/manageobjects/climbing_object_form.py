from django import forms
from objects import get_object_by_id, get_all_active_objects

class ClimbingObjectForm(forms.Form):
    name = forms.CharField(label="Object name", max_length=200, widget=forms.TextInput(attrs={'class':'form-control'}))
    object_id = forms.IntegerField(required=False, label="Id", widget=forms.HiddenInput(attrs={'class':'form-control'}))
    height = forms.FloatField(label="Height", widget=forms.TextInput(attrs={'class':'form-control'}))
    stairs_no = forms.IntegerField(label="Number of stairs", widget=forms.TextInput(attrs={'class':'form-control'}))
