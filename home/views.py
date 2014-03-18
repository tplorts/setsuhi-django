# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django import forms
from django.core.mail import EmailMessage

from setsuhi import settings
import phota



ML_COOKIE_NAME = "ml-language-selection"
ML_CONTEXT_KEY = "ml_active_language"


# This list defines which navigation items will
# appear in the right-hand dock, and the order
# in which they appear, top-to-bottom.
# Each element has three parts:
#   ("view name", "English label", "Japanese label")
nav_list = (
    ("about", "About", "紹介"),
    ("works", "Works", "作品"),
#    ("media", "Media", "画像"),
    ("lessons", "Lessons", "教室"),
    ("contact", "Contact", "連絡"),
)



def ml_selection(request):
    if ML_COOKIE_NAME in request.COOKIES:
        lang = request.COOKIES[ML_COOKIE_NAME]
    else:
        lang = "ja"
    return lang


def multilingual_context( request, context={} ):
    context[ML_CONTEXT_KEY] = ml_selection(request)
    return context


def render_view(request, view_name, context={}):
    context = multilingual_context( request, context )
    context["nav_list"] = nav_list    
    context['present_view_name'] = view_name.split("/")[-1]
    context['use_less_stylesheets'] = settings.TEMPLATE_DEBUG
    return render(request, 'main/'+view_name+'.html', context)



def front(q):
    return render_view(q, 'front')

def about(q):
    return render_view(q, 'pages/about')

def works(q):
    return render_view(q, 'pages/works')

def media(q):
    c = {"phota": phota.photatouse}
    return render_view(q, 'pages/media', c)

def lessons(q):
    return render_view(q, 'pages/lessons')



class ContactForm(forms.Form):
    name = forms.CharField()
    email_address = forms.EmailField()
    telephone_number = forms.CharField(required=False)
    message = forms.CharField()

def contact(request):
    form = None
    sent_message = False
    if "sent" in request.path:
        sent_message = True
    elif request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            name = form.cleaned_data["name"]
            phone = form.cleaned_data["telephone_number"]
            subject = name + "からのお問い合わせ"
            sender = form.cleaned_data["email_address"]
            contact_info = "\n\nメアド："+sender + "\n電話番号："+phone
            body = form.cleaned_data["message"] + contact_info
            sendto = "shiraishi.setsuhi+inquiry@gmail.com"

            email = EmailMessage(subject, body, to=[sendto],
                                 headers = {'Reply-To': sender})
            email.send(fail_silently=False)

            return HttpResponseRedirect('sent/') # Redirect after POST
    else:
        form = ContactForm() # An unbound form

    return render_view(request, 'pages/contact', {
        'form': form,
        'sent_message': sent_message,
    })



def photum(q, photum_index):
    photum_index = int(photum_index)
    if photum_index >= len(phota.photatouse):
        raise Http404
    c = {"photum": phota.photatouse[photum_index]}
    return render_view(q, 'pages/photum', c)
