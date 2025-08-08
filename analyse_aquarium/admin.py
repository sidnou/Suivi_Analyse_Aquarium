from django.contrib import admin

from analyse_aquarium.models import Aquarium, Analyse, Produits

# Register your models here.

# Liste des modèles a afficher
MODELS_SUIVI_ANALYSE_AQUARIUM = [Aquarium, Analyse, Produits]
# Models a affiché
for model_suivi_analysis in MODELS_SUIVI_ANALYSE_AQUARIUM:
    @admin.register(model_suivi_analysis)
    class ModelAdmin(admin.ModelAdmin):
        pass
