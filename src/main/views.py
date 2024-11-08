from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Listing
from .forms import ListingForm


def main_view(request):
    return render(request, "views/main.html", {"name": "AutoMax"})


@login_required
def home_view(request):
    listings = Listing.objects.all()
    context = {
        'listings': listings,
    }
    return render(request, "views/home.html", context)


@login_required
def list_view(request):
    if request.method == ' POST':
        pass
    elif request.method == 'GET':
        listing_form = ListingForm()
        return render(request, 'views/list.html', {'listing_form': listing_form,})