from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Listing
from listings.forms import ContactUsForm
from django.core.mail import send_mail
from django.shortcuts import redirect
from listings.models import BandForm
from listings.models import ListingForm

# ----------- View Band -----------
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

def band_create(request):
	if request.method == 'POST':
		form = BandForm( request.POST)
		if form.is_valid():
			band = form.save()
			return redirect('band-detail', band.id)
	else:
		form = BandForm()
	return render(request, 
		'listings/band_create.html',
		{'form' : form})

def band_change(request, id):
	band = Band.objects.get(id=id)
	if request.method == 'POST':
		form = BandForm(request.POST, instance=band)
		if form.is_valid():
			form.save()
			return redirect('band-detail', band.id)
	else:
		form = BandForm(instance=band) # i fill in the form with data of current band
	return render(request,
		'listings/band_change.html',
		{'form': form})

# ----------- View About -----------
def about(request):
    return render(request, 'listings/about.html')

# ----------- View Listing -----------
def listing_list(request):
	listings = Listing.objects.all()
	return render(request,
		'listings/listing_list.html',
		{'listings': listings})

def listing_detail(request, id):
	listing = Listing.objects.get(id=id)
	return render(request,
		'listings/listing_detail.html',
		{'listing': listing})

def listing_create(request):
	if request.method == 'POST':
		form = ListingForm(request.POST)
		if form.is_valid():
			listing = form.save()
			return redirect('listing-detail', listing.id)
	else:
		form = ListingForm()
	return render(request, 
		'listings/listing_create.html',
		{'form' : form})

def listing_change(request, id):
	listing = Listing.objects.get(id=id)
	if request.method == 'POST':
		form = ListingForm(request.POST, instance=listing)
		if form.is_valid():
			form.save()
			return redirect('listing-detail', listing.id)
	else:
		form = ListingForm(instance=listing) # i fill in the form with data of current band
	return render(request,
		'listings/listing_change.html',
		{'form': form})

# ----------- View Contact -----------
def contact(request):
    return render(request, 'listings/contact.html')

def contact(request):
	if (request.method == 'POST'):
		form = ContactUsForm(request.POST)
		if (form.is_valid()):
			send_mail(
				subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
				message=form.cleaned_data['message'],
				from_email=form.cleaned_data['email'],
				recipient_list=['admin@merchex.xyz'],
			)
			return redirect('email-sent')
	else:
		form = ContactUsForm()
	return render(request,
		'listings/contact.html',
		{'form': form}) 

def email_sent(request):
	return render(request, 'listings/email_sent.html')

# ----------- View error404 -----------
def error404(request, exception):
    return render(request, 'listings/404.html', status=404)