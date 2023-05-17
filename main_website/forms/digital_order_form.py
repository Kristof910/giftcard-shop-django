from django.forms import ModelForm
from ..models.digital_order import DigitalOrder
from django import forms


class DigitalOrderForm(ModelForm):
    email = forms.EmailField(label="Your Email")

    class Meta:
        model = DigitalOrder
        fields = ("email",)
