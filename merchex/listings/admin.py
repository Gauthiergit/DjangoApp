from django.contrib import admin
from listings.models import Band
from listings.models import Listing

# Adjust display of band in table
class BandAdmin(admin.ModelAdmin):
	list_display = ('name', 'year_formed', 'genre')

class ListingAdmin(admin.ModelAdmin):
	list_display = ('title', 'year', 'type', 'band')

# save Band on admin site
admin.site.register(Band, BandAdmin)

admin.site.register(Listing, ListingAdmin)
