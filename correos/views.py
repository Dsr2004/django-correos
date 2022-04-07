import email
import re
from webbrowser import get
from django import views
from django.shortcuts import redirect, render
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages

from django.views.generic import View

def indexs(request):
    return render(request, "index.html")

def contact(request):
    if request.method == "POST":
        nombres = request.POST["nombre"]
        correos = request.POST["correo"]
        comentarios = request.POST["comentario"]
        subject = "Correo de confirmacion de cita"

        template = render_to_string("email_template.html",{
            "name":nombres,
            "email":correos,
            "message": comentarios
        })

        email = EmailMessage(
            subject,
            template,
            settings.EMAIL_HOST_USER,
            ["davitdy2015@gmail.com"]
            )

        email.fail_silently = False
        email.send()

        messages.success(request, "Se ha enviado el correo.")

        return redirect("index")

