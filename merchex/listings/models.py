from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Band(models.Model):
    class Genre(
        models.TextChoices
    ):  # Cette héritage permet de créer une liste de choix
        HIP_HOP = "HH"
        SYNTH_POP = "SP"
        ALTERNATIVE_ROCK = "AR"
        ELECTRO_HARDSTYLE = "HS"
        LATINO = "LT"

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

    def __str__(self):
        return f"{self.title}"
