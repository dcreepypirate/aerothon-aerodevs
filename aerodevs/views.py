from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages  #import messages
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django import forms
from django.conf import settings
from django.shortcuts import redirect
from .models import Product

# import models
from .models import User

# Create your views here.
def index(request):
    return render(request, "aerodevs/home.html")

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "aerodevs/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "aerodevs/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "aerodevs/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "aerodevs/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "aerodevs/register.html")

def dashboard(request):
    product = Product.objects.all()#.order_by('-age')
    part_name_filter = Product.objects.values_list('part_name', flat=True).distinct()
    context = {'product': product, 'part_name_filter':part_name_filter}
    return render(request, 'aerodevs/dashboard.html', context)

#def filter(request):
#    product = Product.objects.values_list('part_name', flat=True).distinct()
#    context = {'part_name_filter': product}
#    return render(request, 'aerodevs/dashboard.html', context)