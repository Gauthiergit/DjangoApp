from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django import forms

# ----------- Model Band -----------
class Band(models.Model):

	# adjust display of band in admin
	def __str__(self):
		return f'{self.name}'
	
	# Create drop-down list 
	class Genre(models.TextChoices):
		HIP_HOP = 'HH'
		SYNTH_POP = 'SP'
		ALTERNATIVE_ROCK = 'AR'
		ROCK_N_ROLL = 'RR'

	name = models.fields.CharField(max_length=100)
	genre = models.fields.CharField(choices=Genre.choices, max_length=5)
	biography = models.fields.CharField(max_length=1000)
	year_formed = models.fields.IntegerField(
	validators=[MinValueValidator(1900), MaxValueValidator(2021)]
	)
	active = models.fields.BooleanField(default=True)
	official_homepage = models.fields.URLField(null=True, blank=True)

# ----------- Model Listing -----------
class Listing(models.Model):

	class Type(models.TextChoices):
		RECORDS = 'RCD'
		CLOTHING = 'CLT'
		POSTERS = 'PST'
		MISCELLANEOUS = 'MSL'

	title = models.fields.CharField(max_length=100)
	description = models.fields.CharField(max_length=1000)
	sold = models.fields.BooleanField(default=False)
	year = models.fields.IntegerField(null=True)
	type = models.fields.CharField(choices=Type.choices, max_length=5)
	# Add Foreign key to create connection with Band
	band = models.ForeignKey(Band, null=True, blank=True, on_delete=models.SET_NULL)

# ----------- Model BandForm -----------
class BandForm(forms.ModelForm):
	class Meta:
		model = Band
		# fields = '__all__'
		exclude = ('active', 'official_homepage')

# ----------- Model ListingForm -----------
class ListingForm(forms.ModelForm):
	class Meta:
		model = Listing
		# fields = '__all__'
		exclude = ('sold',)