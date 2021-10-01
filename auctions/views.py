from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Listing, Images, Comment, Bid

from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import ListingForm, ImagesForm

def index(request):
    return render(request, "auctions/index.html")


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
            messages.error(request, 'Invalid username and/or password.', extra_tags='danger')
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


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
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

@login_required
def listing(request):
    if request.method == "POST":
        
        # Take in data the user submitted and save as forms
        form = ListingForm(request.POST)
        image = ImagesForm(request.POST)

        # Check if data is valid (server-side)
        if (form.is_valid() and image.is_valid()):
                
                # Isolate form and image from the 'cleaned' version of form data. 
                # This step makes sure that any extra data won't be present where it should not be present
                listing = form.cleaned_data
                picture = form.cleaned_data

                # Prepare information to be saved on db
                name = listing['name']
                starting_price = listing['starting_price']
                condition = listing['condition']
                description = listing['description']
                category = listing['category']
                zip_code = listing['zip_code']

                # Assign preorganized info to a variable
                new_listing = Listing(name=name, starting_price=starting_price, condition=condition, description=description, category=category, zip_code=zip_code)

                # Save info to db
                new_listing.save()

                print(listing)


                return HttpResponseRedirect(reverse('listing'))


    else:
        return render(request, "auctions/listing.html", {
            "listing_form": ListingForm(),
            "images_form": ImagesForm()
        })