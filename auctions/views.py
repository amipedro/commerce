from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Listing, Comment, Bid

from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import ListingForm

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
def list(request):
    if request.method == "POST":
        
        # Take in data the user submitted and save as forms
        form = ListingForm(request.POST)

        # Check if data is valid (server-side)
        if form.is_valid():
                
                # Isolate form and image from the 'cleaned' version of form data. 
                # This step makes sure that any extra data won't be present where it should not be present
                listing = form.cleaned_data

                image_url = listing['image_url']

                if image_url.endswith('.jpeg') or image_url.endswith('.jpg') or image_url.endswith('.png') or image_url.endswith('.bmp'):

                    # Prepare information to be saved on db
                    name = listing['name']
                    starting_price = listing['starting_price']
                    condition = listing['condition']
                    description = listing['description']
                    category = listing['category']
                    zip_code = listing['zip_code']
                    # owner_id = request.user.id

                    # Assign preorganized info to a variable
                    new_listing = Listing(name=name, starting_price=starting_price, condition=condition, description=description, 
                                            image_url=image_url, category=category, zip_code=zip_code)
            
                    # Save info to db with owner information
                    new_listing.owner = request.user

                    new_listing.save()
                    return HttpResponseRedirect(reverse('list'))
            
                else:
                    messages.error(request, 'Image url in wrong format. Try adding a link ending in .jpeg, .jpg, .png or .bmp', extra_tags='danger')
                    print("Image url in wrong format")

                    return render(request, "auctions/list.html", {
                        "listing_form": ListingForm(),
                        "message": "Image url in wrong format. Try adding a link ending in .jpeg, .jpg, .png or .bmp"
                    })

    else:

        return render(request, "auctions/list.html", {
            "listing_form": ListingForm()
        })