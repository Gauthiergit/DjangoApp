from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Listing


def band_list(request):
    """Instancie le contenue de la base de donnée dans la variable bands"""
    bands = Band.objects.all()
    """Dans ce chemin en 2nd paramètre pas besoin de mettre "templates/".
    Le dernier paramètre est un dictionnaire contextuel qui devient une
    variable utilisable dans le template."""
    return render(request, "listings/band_list.html", {"bands": bands})


def band_detail(request, band_id):
    band = Band.objects.get(id=band_id)  # On récupère l'id du Band
    return render(request, "listings/band_detail.html", {"band": band})


def about(request):
    return render(request, "listings/about.html")


def listing(request):
    listings = Listing.objects.all()
    return render(request, "listings/listing.html", {"listings": listings})


def contact(request):
    return render(request, "listings/contact.html")
