from django.forms import ModelForm
from ..models.digital_order import DigitalOrder
from django import forms


class DigitalOrderForm(ModelForm):
    email = forms.EmailField(label="Your Email")

    class Meta:
        model = DigitalOrder
        fields = ("payment_method", "email")
        widgets = {
            "payment_method": forms.RadioSelect(
                choices=[
                    ("paypal", "PayPal"),
                    ("creditcard", "Credit Card"),
                    ("banktransfer", "Bank Transfer"),
                ]
            )
        }
