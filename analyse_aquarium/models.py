from django.db import models


# Create your models here.
class Aquarium(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.FloatField()

    def __str__(self):
        return f" {self.name} {self.quantity}"


class Produits(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.FloatField()


class Robinet(models.Model):
    quantity_robinet = models.FloatField(help_text="En %")

    class Meta:
        abstract = True


class Osmose(models.Model):
    quantity_osmose = models.FloatField(help_text="En %")

    class Meta:
        abstract = True


class RemplacementEau(Robinet, Osmose):
    quantity_remplacement_eau = models.FloatField(help_text="En Litre")


class Analyse(RemplacementEau):
    aquarium = models.ForeignKey(Aquarium, on_delete=models.CASCADE)
    nitrite = models.FloatField(help_text="NO2")
    nitrate = models.FloatField(help_text="N03")
    ammonium = models.FloatField(help_text="N04")
    potentiel_hydogene = models.FloatField(help_text="pH")
    hydrotimetrique = models.FloatField(help_text="GH")
    alcalimetrique = models.FloatField(help_text="KH")
    tds = models.FloatField(help_text="TDS")
    temps_eclairage = models.FloatField(help_text="Temps d'eclairage")
    co2 = models.FloatField(help_text="CO2")
    air = models.BooleanField(help_text="Air")
    produits = models.ForeignKey(Produits, on_delete=models.CASCADE)
