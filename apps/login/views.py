# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import User
# from .models import course
from django.shortcuts import render, redirect, reverse
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'login/index.html')

def register(request):
    result = User.objects.validate_registration(request.POST)
    if type(result) == list:
        for error in result:
            messages.error(request, error)
        return redirect('/')
    request.session['user_id'] = result.id
    messages.success(request, "Successfully registered!")
    return redirect ("quote:index")

def login(request):
    result = User.objects.validate_login(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/')
    request.session['user_id'] = result.id
    messages.success(request, "Successfully logged in!")
    return redirect ("quote:index")


def success(request):
    try:
        request.session['user_id']
    except KeyError:
        return redirect('/')
    context = {
        'user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'login/success.html', context)

def show(request, user_id):
    user = User.objects.get(id=user_id)
    unique_ids = user.quotes_left.all().values("quote").distinct()
    unique_quote = []
    for quote in unique_ids:
        unique_quote.append(quote.objects.get(id=quote['quote']))
    context = {
        'user': user,
        'unique_quote_desc': unique_desc
    }
    return render(request, 'login/show.html', context)

def logout(request):
    request.session.clear()
    return redirect('/')
