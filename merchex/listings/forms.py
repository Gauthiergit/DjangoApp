from django import forms
from listings.models import Band
from listings.models import Listing


class ContactUsForm(forms.Form):
    # required=False présise que le champ est facultatif
    name = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField(max_length=1000)


class ListingForm(forms.ModelForm):
    """Création d'un formulaire de création d'objet Listing"""

    class Meta:
        model = Listing
        exclude = ("sold",)


class BandForm(forms.ModelForm):
    """Grâce à l'héritage django.forms.ModelForm, on pourra générer
    un formulaire de création automatiquement à partir de Band"""

    class Meta:
        """Cette sous class spécifie le modèle à utiliser et les champs
        de ce modèle à inclure (tous sauf active et homepage ici)"""

        model = Band
        exclude = ("active", "official_homepage")


"""Si vous voulez exclure certains des autres champs (non nullables) du formulaire,
vous devrez d'abord leur donner une valeur par défaut, ou les rendre nullables,
dans listings/models.py. Vous devrez également effectuer et exécuter une migration
pour mettre à jour le schéma de la base de données, car les valeurs par défaut et
les valeurs NULL sont configurées dans la base de données elle-même."""
