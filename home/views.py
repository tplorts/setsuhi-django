# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import Http404

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
    ("media", "Media", "画像"),
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
    return render(request, 'main/'+view_name+'.html', context)


def front(q):
    return render_view(q, 'front')

def about(q):
    return render_view(q, 'pages/about')

def media(q):
    c = {"phota_names": phota.names}
    return render_view(q, 'pages/media', c)

def lessons(q):
    return render_view(q, 'pages/lessons')

def contact(q):
    return render_view(q, 'pages/contact')


def photum(q, photum_name):
    if photum_name not in phota.names:
        raise Http404
    return render_view(q, 'pages/photum')
