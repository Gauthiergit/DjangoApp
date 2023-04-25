from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return HttpResponse("<h1>Hello Django!</h1>")


def about(request):
    return HttpResponse("<h1>À propos</h1> <p>Nous adorons merch !</p>")


def listing(request):
    return HttpResponse("<h1>Liste des annonces</h1> <p>1er Annonce</p>")


def contact(request):
    return HttpResponse(
        "<h1>Contactez-nous !</h1> <p>Formulaire en cours de création</p>"
    )
