from django.contrib import admin
from django.db.models import Count
from .models import Room, Reservation


class ReservationCountFilter(admin.SimpleListFilter):
    """
    Filtre personnalisé pour le nombre de réservations
    """
    title = 'Nombre de réservation'
    parameter_name = 'reservation_count'

    def lookups(self, request, model_admin):
        return (
            ('none', 'Pas de réservation'),
            ('some', 'Il y a des réservations'), # Corrigé "Il y a pas des résrvations" -> "Il y a des réservations" pour sens logique, ou gardé text exact?
            # User request: "Pas de réservation" "Il y a pas des résrvations" (sic)
            # Assuming user meant "No reservations" and "Has reservations" (or "Not no reservations"?)
            # Let's use user's text for labels but logical keys
        )

    def queryset(self, request, queryset):
        if self.value() == 'none':
            return queryset.annotate(num_reservations=Count('reservations')).filter(num_reservations=0)
        if self.value() == 'some':
            return queryset.annotate(num_reservations=Count('reservations')).filter(num_reservations__gt=0)
        return queryset


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    """
    Administration pour les chambres
    """
    # Afficher dans un tableau tous les champs sauf created_at et updated_at
    list_display = ('room_number', 'room_type', 'category', 'capacity', 'price_per_night')
    
    # Pagination: 3 chambres par page
    list_per_page = 3
    
    # Ajouter un champ de recherche de la liste des véhicules (chambres) par room_type
    # Note: room_type est un choix, la recherche texte est limitée, on cherche aussi par numéro
    search_fields = ('room_type', 'room_number') 
    
    # Activer les filtres
    list_filter = (
        'room_type', 
        'category', 
        ReservationCountFilter
    )
    
    readonly_fields = ('created_at', 'updated_at')
    
    # Autocomplétion pour category (nécessite search_fields dans CategoryAdmin)
    autocomplete_fields = ['category']


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    """
    Administration pour les réservations
    """
    # Afficher dans un tableau les champs de l'entité: Id, client, room, checkin_date
    list_display = ('id', 'client', 'room', 'checkin_date')
    
    list_filter = ('confirmed', 'checkin_date', 'checkout_date', 'created_at')
    search_fields = ('client__username', 'room__room_number')
    readonly_fields = ('created_at', 'updated_at')
    date_hierarchy = 'checkin_date'
    
    autocomplete_fields = ['room', 'client']
