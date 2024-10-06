from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Listing

def band_list(request):
	bands = Band.objects.all()
	return render(request,
		'listings/band_list.html',
        {'bands': bands})

def band_detail(request, id):
	band = Band.objects.get(id=id)
	return render(request,
		'listings/band_detail.html',
		{'band': band})

def about(request):
    return render(request, 'listings/about.html')

def listings(request):
    listing = Listing.objects.all()
    return render(request, 'listings/listings.html', {'listings': listing})

def contact(request):
    return render(request, 'listings/contact.html')

def error404(request, exception):
    return render(request, '404.html', status=404)
