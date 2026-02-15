# Django Hotel Management System

Un système complet de gestion de réservation d'hôtel développé avec Django.

## 🚀 Fonctionnalités

### 🏢 BackOffice (Administration)
- **Gestion des Clients**
  - Identifiants clients uniques
  - Validation des emails (@gmail.com obligatoire)
- **Gestion des Chambres**
  - Catégorisation flexible (Standard, Deluxe, Suite, etc.)
  - Validation regex des numéros de chambre
  - Tarification dynamique
- **Gestion des Réservations**
  - Vérification des disponibilités
  - Calcul automatique des coûts et durées
- **Dashboard Personnalisé**
  - Filtres avancés (par type, catégorie, statut réservation)
  - Recherche globale
  - Pagination optimisée
  - Autocomplétion pour les relations

### 🌐 FrontOffice (Site Client)
- Liste des chambres disponibles
- Tri automatique par capacité
- Affichage clair des prix et options

## 🛠️ Installation

### Prérequis
- Python 3.8+
- pip

### 1. Cloner le projet
```bash
git clone https://github.com/AbdelhafidhGHARBI/NomDuRepo.git
cd django_project
```

### 2. Créer un environnement virtuel
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Installer les dépendances
```bash
pip install django
```

### 4. Appliquer les migrations
```bash
python manage.py migrate
```

### 5. Créer un superutilisateur (Optionnel)
```bash
python manage.py createsuperuser
```

### 6. Lancer le serveur
```bash
python manage.py runserver
```
Accédez à l'application sur : http://127.0.0.1:8000/

## 📦 Structure du Projet

- **ClientApp** : Gestion des utilisateurs et profils clients.
- **CategoryApp** : Gestion des typologies de chambres.
- **RoomApp** : Cœur du système (Chambres, Réservations, Vues FrontOffice).

## 🔒 Règles de Validation

- **Emails** : Domaine `gmail.com` uniquement.
- **Chambres** : Format `Room[Lettre][Chiffres]` (ex: RoomA101).
- **Catégories** : Nom entre 10 et 100 caractères.
- **Réservations** : Dates cohérentes (Check-out > Check-in).

## 👤 Auteur
**Abdelhafidh GHARBI**
