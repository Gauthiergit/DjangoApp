from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Band(models.Model):
    class Genre(
        models.TextChoices
    ):  # Cette héritage permet de créer une liste de choix
        HIP_HOP = "HH"
        SYNTH_POP = "SP"
        ALTERNATIVE_ROCK = "AR"
        PUNK_ROCK = "PR"
        ELECTRO = "EL"

    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(choices=Genre.choices, max_length=5)
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2023)]
    )
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(
        null=True, blank=True
    )  # Autorise les valeurs nuls si un groupe n'a pas de sites

    def __str__(self):
        return f"{self.name}"


class Listing(models.Model):
    class Type(models.TextChoices):
        RECORDS = "REC"
        CLOTHING = "CLT"
        POSTERS = "PST"
        MISCELLANEOUS = "MIS"

    title = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=1000)
    sold = models.fields.BooleanField(default=False)
    year = models.fields.IntegerField()
    type = models.fields.CharField(choices=Type.choices, max_length=5)
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)
    # .Foreingnkey permet de créer un lien avec l'objet Band et créra une liste déroulante dans database
    # null=  permet de laisser bande vide si aucun lien n'est souhaité
    # on_delete permet que si l'objet Band est supprimé, band sera considéré comme nul et on ne supprimera pas l'objet Listing

    def __str__(self):
        return f"{self.title}"
