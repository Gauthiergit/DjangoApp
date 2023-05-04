from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Listing
from listings.forms import ContactUsForm
from django.core.mail import send_mail
from django.shortcuts import redirect


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
    """L'instruction 'if' permet de créer un fomualire dans le modèle qu'il soit rempli ou non.
    Elle permet aussi de générer des messages d'erreur en fonction de nos règles modèle (forms.py)
    """
    if request.method == "POST":
        # Créer une instance de notre formulaire et le remplir avec les données POST
        form = ContactUsForm(request.POST)

        if form.is_valid():
            send_mail(
                # form.cleaned_data est un dictionnaire contenant les données après validation par .is-valid().
                subject=f'Message from {form.cleaned_data["name"] or "anonymous"} via Merchex Contact Us form',
                message=form.cleaned_data["message"],
                from_email=form.cleaned_data["email"],
                recipient_list=["admin@merchex.xyz"],
            )
            return redirect("email-sent")
            # L'utilisateur sera redirigé vers une page de confirmation après l'envoi
    else:
        # Ceci doit être une requête GET, donc créer un fomulaire vide
        form = ContactUsForm()  # Ajout d'un formulaire.
    # Le dictionnaire contextuel en dernier paramètre passe ce formulaire au gabarit.
    return render(request, "listings/contact.html", {"form": form})


def email_sent(request):
    return render(request, "listings/email_sent.html")
