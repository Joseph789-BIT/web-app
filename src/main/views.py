from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Listing


def main_view(request):
    return render(request, "views/main.html", {"name": "ShowBlitz"})


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
        return render(request, 'views/main.html', {})