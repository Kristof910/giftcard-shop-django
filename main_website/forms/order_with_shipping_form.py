from django import forms
from django.forms import ModelForm
from ..models.order_with_shipping import OrderWithShipping


class OrderWithShippingForm(ModelForm):
    email = forms.EmailField(label="Your Email")
    name = forms.CharField(label="Your Name")
    phone = forms.IntegerField(
        label="Phone Number", widget=forms.TextInput(attrs={"type": "number"})
    )
    country = forms.CharField(label="Country")
    county = forms.CharField(label="County")
    address = forms.CharField(label="Address")

    class Meta:
        model = OrderWithShipping
        fields = (
            "payment_method",
            "email",
            "name",
            "phone",
            "country",
            "county",
            "address",
        )
        widgets = {
            "payment_method": forms.RadioSelect(
                choices=[
                    ("paypal", "PayPal"),
                    ("creditcard", "Credit Card"),
                    ("banktransfer", "Bank Transfer"),
                ]
            )
        }
