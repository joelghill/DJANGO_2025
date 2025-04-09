from django import forms

from home.models.address import Address


class AddressForm(forms.ModelForm):

    class Meta:
        model = Address
        exclude = []

    
    