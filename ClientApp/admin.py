from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Client


@admin.register(Client)
class ClientAdmin(UserAdmin):
    """
    Administration personnalisée pour le modèle Client
    """
    # Afficher dans le tableau les champs: client_id, first_name et last_name
    list_display = ('client_id', 'first_name', 'last_name', 'email', 'username')
    
    # Ajouter un champ de recherche de la liste des clients_id
    search_fields = ('client_id', 'username', 'email')
    
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'date_joined')
    readonly_fields = ('created_at', 'updated_at', 'date_joined', 'last_login')
    
    fieldsets = UserAdmin.fieldsets + (
        ('Informations Supplémentaires', {
            'fields': ('client_id', 'created_at', 'updated_at')
        }),
    )
    
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Informations Client', {
            'fields': ('client_id', 'email', 'first_name', 'last_name')
        }),
    )
