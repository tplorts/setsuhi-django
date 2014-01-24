from django.shortcuts import render

def front(q):
    return render(q, 'main/front.html', {})
