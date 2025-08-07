from django.db import models


# Create your models here.
class Aquarium(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()

    def __str__(self):
        return f" {self.name} {self.quantity}"


class Produits(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()


class Robinet(models.Model):
    quantity_robinet = models.IntegerField(help_text="En %")

    class Meta:
        abstract = True


class Osmose(models.Model):
    quantity_osmose = models.IntegerField(help_text="En %")

    class Meta:
        abstract = True


class RemplacementEau(Robinet, Osmose):
    quantity_remplacement_eau = models.IntegerField(help_text="En Litre")


class Analyse(RemplacementEau):
    aquarium = models.ForeignKey(Aquarium, on_delete=models.CASCADE)
    nitrite = models.IntegerField(help_text="NO2")
    nitrate = models.IntegerField(help_text="N03")
    ammonium = models.IntegerField(help_text="N04")
    potentiel_hydogene = models.IntegerField(help_text="pH")
    hydrotimetrique = models.IntegerField(help_text="GH")
    alcalimetrique = models.IntegerField(help_text="KH")
    tds = models.IntegerField(help_text="TDS")
    temps_eclairage = models.IntegerField(help_text="Temps d'eclairage")
    co2 = models.IntegerField(help_text="CO2")
    air = models.BooleanField(help_text="Air")
    produits = models.ForeignKey(Produits, on_delete=models.CASCADE)
