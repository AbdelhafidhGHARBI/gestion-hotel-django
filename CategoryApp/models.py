from django.db import models
from django.core.validators import MinLengthValidator

class Category(models.Model):
    """
    Modèle pour les catégories de chambres
    """
    # id est auto-généré par Django comme clé primaire
    category_name = models.CharField(
        max_length=100, 
        unique=True,
        validators=[MinLengthValidator(10, message="Le nom de la catégorie doit contenir entre 10 et 100 caractères.")],
        error_messages={
            'max_length': "Le nom de la catégorie doit contenir entre 10 et 100 caractères.",
            'unique': "Une catégorie avec ce nom existe déjà."
        }
    )
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Catégorie"
        verbose_name_plural = "Catégories"
        ordering = ['category_name']
    
    def __str__(self):
        return self.category_name
