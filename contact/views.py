from django.shortcuts import render, redirect
from .models import Contact
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.

def contact_us(request):
    """ View for rendering contact us page"""

    if request.method == "POST":
        if request.POST.get("txtName") and request.POST.get("txtEmail"):
            post = Contact()
            post.full_name = request.POST.get("txtName")
            post.email = request.POST.get("txtEmail")
            post.phone_number = request.POST.get("txtPhone")
            post.message = request.POST.get("txtMsg")
            post.save()

            subject = "Tast World Snacks Contact Form"
            message = post.message = request.POST.get(
                "txtMsg") + " From: " + post.full_name + " Sender's Email Address " + post.email
            from_email = "tasteworldsnacks@example.com"
            if subject and message and from_email:
                try:
                    send_mail(subject, message, from_email, ['cecilia4binck@gmail.com'])
                except BadHeaderError:
                    return HttpResponse("Invalid Header Found")
                return render(request, "contact/contact_success.html")
            return HttpResponse("Make sure all fields are entered and valid.")
        return render(request, "contact/contact_success.html")

    return render(request, "contact/contact_us.html")
