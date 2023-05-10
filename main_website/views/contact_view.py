from django.shortcuts import render
from django.shortcuts import redirect
from ..forms.contact_form import ContactForm
from ..models import ContactMessages


# using method based view because there are no models required
def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]
            contact_message = ContactMessages(name=name, email=email, message=message)
            contact_message.save()
        return redirect("index")
    else:
        form = ContactForm()
    return render(request, "contact.html", {"form": form})
