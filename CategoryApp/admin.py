from django.contrib import admin
from .models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Administration pour les catégories de chambres
    """
    # Afficher dans un tableau tous les champs sauf created_at et updated_at
    list_display = ('id', 'category_name', 'description')
    
    # Ajouter un champ de recherche de la liste des catégories par category_name
    search_fields = ('category_name',)
    
    readonly_fields = ('created_at', 'updated_at')
