from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.views import View

class SendMailPage(View):
    def get(self, request):
        return render(request, "main/mail.html")
    
    def post(self, request):
        context = {}

        address = request.POST.get("address")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        if address and subject and message:
            try:
                send_mail(subject, message, settings.EMAIL_HOST_USER,[address])
                context["result"] = "successfully"
            except Exception as e:
                context["result"] = f"error:{e}"
        else:
            context["result"] = "All fields are reqired"
        return render(request, "main/mail.html", context=context)