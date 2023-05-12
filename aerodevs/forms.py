from django import forms

class ProductFilterForm(forms.Form):
    name = forms.CharField(required=False, label='Name')
    material = forms.CharField(required=False, label='Material')
    age = forms.IntegerField(required=False, label='Age')
    manufacturer = forms.CharField(required=False, label='Manufacturer')
