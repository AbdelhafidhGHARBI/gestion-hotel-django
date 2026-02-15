from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
import re

def validate_gmail(value):
    """
    Validateur personnalisé pour vérifier que l'email appartient au domaine gmail.com
    """
    if not re.match(r'^[\w\.-]+@gmail\.com$', value):
        raise ValidationError("Veuillez entrer une adresse email valide appartenant au domaine gmail.com (ex: example@gmail.com)")

class Client(AbstractUser):
    """
    Modèle Client qui hérite de AbstractUser.
    client_id est la clé primaire.
    """
    client_id = models.CharField(max_length=100, primary_key=True)
    
    # Surcharge du champ email pour ajouter les contraintes
    email = models.EmailField(
        unique=True,
        validators=[validate_gmail],
        error_messages={
            'unique': "Un client avec cet email existe déjà.",
        }
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"
    
    def save(self, *args, **kwargs):
        # Générer automatiquement client_id basé sur username si vide
        if not self.client_id and self.username:
            self.client_id = f"CLT-{self.username}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.username} - {self.first_name} {self.last_name}"
