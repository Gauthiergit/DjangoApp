from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Listing
from listings.forms import ContactUsForm


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


def listing_list(request):
    listings = Listing.objects.all()
    return render(request, "listings/listing_list.html", {"listings": listings})


def listing_detail(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    return render(request, "listings/listing_detail.html", {"listing": listing})


def contact(request):
    form = ContactUsForm()  # Ajout d'un formulaire.
    """Le dictionnaire contextuel en dernier paramètre passe ce formulaire au gabarit"""
    return render(request, "listings/contact.html", {"form": form})
