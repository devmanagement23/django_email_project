from collections import UserDict
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.

def home(request):
    subject = 'welcome to Hello world'
    message = f'Hi thank you for sending mail with django .'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['devinder232323@gmail.com','worldaround555@gmail.com' ]
    send_mail( subject, message, email_from, recipient_list )

    return HttpResponse("Email send successully")