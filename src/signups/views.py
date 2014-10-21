#python first
#django second
#your apps
#local apps
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect
# Create your views here.

from .forms import SignUpForm

def home(request):

    form = SignUpForm(request.POST or None)

    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()

        #send_mail(subject, message, from_email, to_list, fail_silently=True)
        subject = 'Thank you!'
        message = 'Super! Voll geil Alter danke dir fett'
        from_email = settings.EMAIL_HOST_USER
        to_list = [save_it.email, settings.EMAIL_HOST_USER]
        send_mail(subject, message, from_email, to_list, fail_silently=True)
        messages.success(request, 'Thank you for Joining!')
        return HttpResponseRedirect ('/thank-you/')
    return render_to_response("signup.html",
                              locals(),
                              context_instance=RequestContext(request))


def thankyou(request):

    form = SignUpForm(request.POST or None)

    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
        messages.success(request, 'Thank you for Joining!')
        return HttpResponseRedirect ('/thank-you/')

    return render_to_response("thankyou.html",
                              locals(),
                              context_instance=RequestContext(request))

def about(request):


    return render_to_response("about.html",
                              locals(),
                              context_instance=RequestContext(request))