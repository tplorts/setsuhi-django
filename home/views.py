from django.shortcuts import render

ML_COOKIE_NAME = "ml-language-selection"
ML_CONTEXT_KEY = "ml_active_language"

def ml_selection(request):
    if ML_COOKIE_NAME in request.COOKIES:
        lang = request.COOKIES[ML_COOKIE_NAME]
    else:
        lang = "en"
    return lang


def view_with_ml(request, view_name, context={}):
    context[ML_CONTEXT_KEY] = ml_selection(request)
    context['present_view_name'] = view_name
    return render(request, 'main/'+view_name+'.html', context)


def front(q):
    return view_with_ml(q, 'front')

def about(q):
    return view_with_ml(q, 'pages/about')

def media(q):
    return view_with_ml(q, 'pages/media')

def lessons(q):
    return view_with_ml(q, 'pages/lessons')

def contact(q):
    return view_with_ml(q, 'pages/contact')
