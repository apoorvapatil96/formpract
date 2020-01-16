from django.shortcuts import render
from django.utils.html import  strip_tags
from django.template.loader import  render_to_string
# Create your views here.
from django.core import mail
import smtplib
def sendmail(request):
    score=2
    connection=mail.get_connection()
    connection.open()
    email1=mail.EmailMessage('hello','body goes here',
                             'apoorvaypatil@gmail.com',
                             ['patilapoo00@gmail.com'],
                             connection-connection,
                             )
    email1.send()
