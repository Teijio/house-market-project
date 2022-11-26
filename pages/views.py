from django.shortcuts import render
from django.http import HttpResponse

from listings.models import Listing
from listings.models import Realtor

def index(request):
    listings = Listing.objects.filter(is_published=True)[:3]
    context = {
        "listings": listings,
    }
    return render(request, "pages/index.html", context)


def about(request):
    realtors = Realtor.objects.all()
    context = {
        "realtors": realtors,
    }
    return render(request, "pages/about.html", context)
