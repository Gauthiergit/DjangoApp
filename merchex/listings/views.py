from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Listing


def hello(request):
    """Instancie le contenue de la base de donnée dans la variable bands"""
    bands = Band.objects.all()
    """Dans ce chemin en 2nd paramètre pas besoin de mettre "templates/".
    Le dernier paramètre est un dictionnaire contextuel qui devient une
    variable utilisable dans le template."""
    return render(request, "listings/hello.html", {"bands": bands})


def about(request):
    return render(request, "listings/about.html")


def listing(request):
    listings = Listing.objects.all()
    return render(request, "listings/listing.html", {"listings": listings})


def contact(request):
    return render(request, "listings/contact.html")
