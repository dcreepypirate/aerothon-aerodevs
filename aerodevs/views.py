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
from .models import User
from django.db.models import Sum
from json import dumps


def home(request):
    return render(request, "aerodevs/home.html")

@login_required
def market(request):
    product = Product.objects.all()#.order_by('-age')
    part_name_filter = Product.objects.values_list('part_name', flat=True).distinct()
    context = {'product': product, 'part_name_filter':part_name_filter}
    return render(request, 'aerodevs/market.html', context)


def dashboard(request):
    product = Product.objects.all()  # .order_by('-age')
    part_name_filter = Product.objects.values_list('part_name', flat=True).distinct()
    value = round((Product.objects.aggregate(Sum('Percentage_recycled'))[
                  'Percentage_recycled__sum'])*100, 2)
    # no_rows = Product.objects.filter(username='myname', status=0).count()
    one = Product.objects.filter(age__gte=0, age__lte=10).count()
    two = Product.objects.filter(age__gte=10, age__lte=20).count()
    three = Product.objects.filter(age__gte=20, age__lte=30).count()
    four = Product.objects.filter(age__gte=30, age__lte=40).count()
    five = Product.objects.filter(age__gte=40, age__lte=50).count()

    array = [one, two, three, four, five]

    manufacturers = ['Boeing', 'Embraer', 'Cessna', 'Gulfstream', 'Airbus']
    carbonarray = []
    energy_saved = []

    for manufacturer in manufacturers:
        total_carbon_saved = Product.objects.filter(manufacturer=manufacturer).aggregate(
            Sum('Carbon_Footprint_Saved'))['Carbon_Footprint_Saved__sum']
        carbonarray.append(total_carbon_saved or 0)

        saved_energy = Product.objects.filter(manufacturer=manufacturer).aggregate(
            Sum('Energy_Consumption_Saved'))['Energy_Consumption_Saved__sum']
        energy_saved.append(saved_energy or 0)

    part_name_filter = Product.objects.values_list('part_name', flat=True).distinct()

    context = {'product': product, 'part_name_filter': part_name_filter, 'value': value, 'one': one, 'array': array,
               'carbon': carbonarray, 'energy_saved':energy_saved, 'part_name_filter':part_name_filter}
    return render(request, 'aerodevs/dashboard.html', context)


@login_required
def index(request):

    if not request.user.is_authenticated:
        return redirect(login_view)

    current_user = request.user
    user = User.objects.get(username = current_user)

    if user.role == "M" or user.role=="R":
        return redirect(market)
        
    else:
        return redirect(dashboard)


def buy(request,part_id):
    part = Product.objects.get(part_id=part_id)
    part.is_Sold=True
    part.save()
    return redirect("/market")

def search(request):
    query = request.GET['search']
    product = Product.objects.filter(part_name__icontains=query)
    part_name_filter = Product.objects.values_list(
        'part_name', flat=True).distinct()
    context = {'product': product, 'part_name_filter': part_name_filter}
    return render(request, 'aerodevs/search.html', context)




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
    return HttpResponseRedirect(reverse("login"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        role= request.POST["role"]
        if password != confirmation:
            return render(request, "aerodevs/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email=email, password=password, role=role)
            user.save()
        except IntegrityError:
            return render(request, "aerodevs/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "aerodevs/register.html")



