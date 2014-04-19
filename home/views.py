# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django import forms
from django.core.mail import EmailMessage

from setsuhi import settings
import models



# This list defines which navigation items will
# appear in the right-hand dock, and the order
# in which they appear, top-to-bottom.
# Each element has three parts:
#   ("view name", "English label", "Japanese label")
nav_list = (
    ("about",    "About",    "紹介", ""),
    ("pictures", "Pictures", "写真", ""),
    ("videos",   "Videos",   "動画", ""),
    ("schedule", "Events",   "予定", ""),
    ("lessons",  "Lessons",  "教室", ""),
    ("contact",  "Contact",  "連絡", ""),
    ("blog",     "Blog",     "ブログ", "target=\"_blank\""),
)



def ml_selection(request):
    if settings.ML_COOKIE_NAME in request.COOKIES:
        lang = request.COOKIES[settings.ML_COOKIE_NAME]
    else:
        lang = settings.ML_DEFAULT_LANGUAGE
    return lang


def multilingual_context( request, context={} ):
    context[settings.ML_CONTEXT_KEY] = ml_selection(request)
    return context


def render_page(request, page_name, context={}):
    context = multilingual_context( request, context )
    context["nav_list"] = nav_list
    context['present_page_name'] = page_name.split("/")[-1]
    context['isProduction'] = settings.isProduction
    context['use_less_stylesheets'] = settings.TEMPLATE_DEBUG
    return render(request, 'pages/' + page_name + '.html', context)



def front(q):
    return render_page(q, 'front')

def about(q):
    return render_page(q, 'about')

def pictures(q):
    g = models.SakuhinGroup.objects.filter(is_shown=True).order_by("order_index")
    c = {"sakuhin_groups": g}
    return render_page(q, 'pictures', c)

def videos(q):
    return render_page(q, 'videos')

def schedule(q):
    return render_page(q, 'schedule')

def lessons(q):
    return render_page(q, 'lessons')




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

    return render_page(request, 'contact', {
        'form': form,
        'sent_message': sent_message,
    })





def edit_sakuhin_info( request ):
    if request.method != "POST":
        response = "Please use POST"
    else:
        form = models.SakuhinInfoForm( request.POST )
        if not form.is_valid():
            response = "Maybe there was a mistake"
        else:
            pk = form.cleaned_data["dbpk"]
            try:
                sakuhin = models.Sakuhin.objects.get( id=pk )
            except Exception:
                response = "I can't find that piece"
            else:
                if not sakuhin.updateInfo( form ):
                    response = "Something broke"
                else:
                    response = "A-OK"
    return HttpResponse(response)
