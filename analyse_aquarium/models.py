from django.db import models


# Create your models here.
class Aquarium(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=False, null=False)
    quantity = models.FloatField()

    def __str__(self):
        return f" {self.name} {self.quantity}"


class Produits(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, unique=True)
    quantity = models.FloatField(help_text="en ml", null=False, blank=False)


class Robinet(models.Model):
    quantity_robinet = models.FloatField(help_text="En %")

    class Meta:
        abstract = True


class Osmose(models.Model):
    quantity_osmose = models.FloatField(help_text="En %")

    class Meta:
        abstract = True


class RemplacementEau(Robinet, Osmose):
    quantity_remplacement_eau = models.FloatField(help_text="En Litre", null=False, blank=False)


class Analyse(RemplacementEau):
    aquarium = models.ForeignKey(Aquarium, on_delete=models.CASCADE)
    nitrite = models.FloatField(help_text="NO2", null=True, blank=True)
    nitrate = models.FloatField(help_text="N03", null=True, blank=True)
    ammonium = models.FloatField(help_text="N04", null=True, blank=True)
    potentiel_hydogene = models.FloatField(help_text="pH", null=True, blank=True)
    hydrotimetrique = models.FloatField(help_text="GH", null=True, blank=True)
    alcalimetrique = models.FloatField(help_text="KH", null=True, blank=True)
    tds = models.FloatField(help_text="TDS", null=True, blank=True)
    temps_eclairage = models.FloatField(help_text="Temps d'eclairage", null=True, blank=True)
    co2 = models.FloatField(help_text="CO2 en mg/s", null=True, blank=True)
    air = models.BooleanField(help_text="Air", null=True, blank=True)
    produits = models.ForeignKey(Produits, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return (f"{self.aquarium.name} "
                f"{self.nitrite} "
                f"{self.nitrate} "
                f"{self.ammonium} "
                f"{self.potentiel_hydogene} "
                f"{self.hydrotimetrique} "
                f"{self.alcalimetrique} "
                f"{self.tds} "
                f"{self.temps_eclairage} "
                f"{self.co2} "
                f"{self.air}"
                f"{self.quantity_robinet} "
                f"{self.quantity_osmose} "
                f"{self.quantity_remplacement_eau} "
                f"{self.produits} ")
# Les remarque du LLM
class Remarque(models.Model):
    pass
# Les taches que le LLM demande de faire
class Tache(models.Model):
    pass