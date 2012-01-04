from django.shortcuts import render_to_response
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
#from django.views.decorators.csrf import csrf_exempt
#from django.core.context_processors import csrf
from django.template import RequestContext
import string


def home(request):
    return render_to_response('base.html')

def cv(request):
    return render_to_response('cv.html')

def projects(request):
    return render_to_response('projects.html')

def links(request):
    return render_to_response('links.html')

def quotes(request):
    return render_to_response('quotes.html')

def blog(request):
    return render_to_response('blog.html')

def contact(request):
    return render_to_response('contact.html')

def derain(request):
    return render_to_response('derain.html')

def send_email(request):
    subject = request.GET.get('subject')
    message = request.GET.get('message')
    from_email = request.GET.get('from_email')
    to = "jsmoxon@gmail.com"
    body = string.join((
        "From: %s" % from_email,
        "To: %s" % to,
        "Subject: %s" % subject
        ,
        message,
        ), "\r\n")
    send_mail(subject, body, from_email, ['jsmoxon@gmail.com'], fail_silently=False)
   # return HttpResponse("Thanks! I'll be in touch")
    return HttpResponseRedirect('/')

def cron_email():
    subject = "Here is the subject"
    message = "Have you ever read Black Marigolds?"
    from_email = "test@test.com"
    to = "jsmoxon@gmail.com"
    body = string.join((
        "From: %s" % from_email,
        "To: %s" % to,
        "Subject: %s" % subject
        ,
        message,
        ), "\r\n")
    send_mail(subject, body, from_email, ['jsmoxon@gmail.com'], fail_silently=False)
