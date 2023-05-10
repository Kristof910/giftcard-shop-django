from django.forms import ModelForm
from ..models.contact_message import ContactMessage
from django import forms


class ContactForm(ModelForm):
    name = forms.CharField(label="Your Name", max_length=30)
    email = forms.EmailField(label="Your Email")
    message = forms.CharField(label="Message", widget=forms.Textarea)

    class Meta:
        model = ContactMessage
        fields = ("name", "email", "message")
