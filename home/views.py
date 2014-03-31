# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django import forms
from django.core.mail import EmailMessage

from setsuhi import settings



ML_COOKIE_NAME = "ml-language-selection"
ML_CONTEXT_KEY = "ml_active_language"


# This list defines which navigation items will
# appear in the right-hand dock, and the order
# in which they appear, top-to-bottom.
# Each element has three parts:
#   ("view name", "English label", "Japanese label")
nav_list = (
    ("about",    "About",    "紹介", ""),
#    ("works",    "Works",    "作品", ""),
#    ("photos",   "Photos",   "写真", ""),
    ("schedule", "Schedule", "予定", ""),
    ("lessons",  "Lessons",  "教室", ""),
    ("contact",  "Contact",  "連絡", ""),
    ("blog",     "Blog",     "ブログ", "target=\"_blank\""),
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
    context['isProduction'] = settings.isProduction
    context['use_less_stylesheets'] = settings.TEMPLATE_DEBUG
    return render(request, 'main/'+view_name+'.html', context)



def front(q):
    return render_view(q, 'front')

def about(q):
    return render_view(q, 'pages/about')

def works(q):
    return render_view(q, 'pages/works')

def photos(q):
    return render_view(q, 'pages/photos')

def schedule(q):
    return render_view(q, 'pages/schedule')

def lessons(q):
    return render_view(q, 'pages/lessons')




class TelephoneInput( forms.TextInput ):
    input_type = 'tel'

class ContactForm(forms.Form):
    name = forms.CharField()
    email_address = forms.EmailField()
    telephone_number = forms.CharField(widget=TelephoneInput, required=False)
    message = forms.CharField(widget=forms.Textarea)

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


