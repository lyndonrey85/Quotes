# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Quote
from ..login.models import User
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
def index(request):
    quotes = Quote.objects.all()
    current_user = User.objects.get(id=request.session["user_id"])
    user_favorites = current_user.favorites.all()
    # course_delete = Course.objects.all().delete()
    context = {
        "quotes": quotes,
        "favorites": user_favorites
        # "course_to_remove": course_remove
    }
    return render(request, 'quote/index.html', context)

def create(request):
    current_user = User.objects.get(id=request.session["user_id"])
    new_quotes = Quote.objects.create(
        quoted_by=request.POST["quoted_by"],
        message=request.POST["message"],
        creator=current_user)
    return redirect("quote:index")

def delete(request, quote_id):
    quote = Quote.objects.get(id=quote_id)
    current_user = User.objects.get(id=request.session["user_id"])
    quote.delete()
    # quote_remove.remove()
    return redirect("quote:index")

def favorite(request, quote_id):
    current_user = User.objects.get(id=request.session["user_id"])
    current_quote = Quote.objects.get(id=quote_id)
    current_quote.user_favorites.add(current_user)
    current_quote.save()
    return redirect("quote:index")

def show(request, quote_id):
    current_quote = Quote.objects.get(id=quote_id)
    context = {
        "quote":current_quote
    }
    return render(request, "quote/show.html", context)