from django.db import models
from django.core.validators import MinValueValidator, RegexValidator
from django.core.exceptions import ValidationError
from django.conf import settings
from django.utils import timezone
from CategoryApp.models import Category
import datetime

class Room(models.Model):
    """
    Modèle pour les chambres d'hôtel
    """
    ROOM_TYPE_CHOICES = [
        ('simple', 'Simple'),
        ('suite', 'Suite'),
    ]
    
    room_number_validator = RegexValidator(
        regex=r'^Room[a-zA-Z]\d+$',
        message='Le numéro de la chambre n\'est pas valide.'
    )

    room_number = models.CharField(
        max_length=20, 
        unique=True,
        validators=[room_number_validator]
    )
    room_type = models.CharField(max_length=10, choices=ROOM_TYPE_CHOICES)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='rooms')
    capacity = models.IntegerField(validators=[MinValueValidator(1)])
    price_per_night = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Chambre"
        verbose_name_plural = "Chambres"
        ordering = ['room_number']
    
    def __str__(self):
        return f"Chambre {self.room_number} - {self.get_room_type_display()}"


class Reservation(models.Model):
    """
    Modèle pour les réservations
    """
    client = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='reservations'
    )
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='reservations')
    checkin_date = models.DateField()
    checkout_date = models.DateField()
    confirmed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Réservation"
        verbose_name_plural = "Réservations"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Réservation {self.id} - {self.client.username} - Chambre {self.room.room_number}"
    
    def clean(self):
        """
        Validations personnalisées pour les dates
        """
        # Validation 1: Checkin date must be today or future
        if self.checkin_date:
            if self.checkin_date < timezone.now().date():
                raise ValidationError("La date d'arrivée doit être la date du jour ou ultérieure.")
        
        # Validation 2: Checkout date must be >= checkin date
        if self.checkout_date and self.checkin_date:
            if self.checkout_date < self.checkin_date:
                 # Note: User request says "doit etre postérieur ou égale", so < is strictly invalid. 
                 # Wait, usually a hotel stay is at least 1 night. 
                 # But user said "postérieur ou égale à la date d'arrivée".
                 # If equal, it's 0 nights? Technically user prompt says "postérieur ou égale".
                 # The error message requested: "La date de départ doit être postérieure ou égale à la date d'arrivée."
                raise ValidationError("La date de départ doit être postérieure ou égale à la date d'arrivée.")

    def save(self, *args, **kwargs):
        self.full_clean() # Force validation on save
        super().save(*args, **kwargs)

    def total_nights(self):
        """Calcule le nombre de nuits"""
        if self.checkout_date and self.checkin_date:
            return (self.checkout_date - self.checkin_date).days
        return 0
    
    def total_price(self):
        """Calcule le prix total de la réservation"""
        return self.room.price_per_night * self.total_nights()
