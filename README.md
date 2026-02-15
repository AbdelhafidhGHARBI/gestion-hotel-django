# 🏨 Système de Gestion Hôtelière (Django)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Django](https://img.shields.io/badge/Django-5.0%2B-green)
![License](https://img.shields.io/badge/License-MIT-purple)

Une application web complète et robuste pour la gestion des réservations d'hôtel, incluant un FrontOffice pour les clients et un BackOffice riche pour l'administration.

---

## 📑 Table des Matières
- [Fonctionnalités](#-fonctionnalités)
- [Architecture Technique](#-architecture-technique)
- [Installation et Démarrage](#-installation-et-démarrage)
- [Guide d'Utilisation](#-guide-dutilisation)
- [Règles de Validation](#-règles-de-validation)
- [Auteur](#-auteur)

---

## 🚀 Fonctionnalités

### 🏛️ BackOffice (Administration)
L'interface d'administration a été entièrement personnalisée pour une gestion efficace.

#### **Gestion des Clients**
- **Tableau de bord :** Vue détaillée avec ID client, nom, prénom et email.
- **Recherche :** Barre de recherche intuitive (par ID, nom d'utilisateur, email).
- **Sécurité :** Validation stricte des emails (domaine `@gmail.com` obligatoire).
- **Génération d'ID :** Création automatique d'identifiants uniques (ex: `CLT-username`).

#### **Gestion des Chambres**
- **Flexibilité :** Support de multiples types (Simple, Suite) et catégories personnalisables.
- **Organisation :** Pagination (3 par page) et tri par défaut.
- **Filtres Avancés :**
  - Par Type de chambre
  - Par Catégorie
  - **Filtre "Réservation"** : Permet de voir rapidement les chambres avec ou sans activité.
- **Ergonomie :** Autocomplétion pour la sélection des catégories.

#### **Gestion des Réservations**
- **Suivi :** Vue claire des réservations avec statut (Confirmé/En attente).
- **Logique Métier :**
  - Calcul automatique du nombre de nuits.
  - Calcul automatique du prix total.
  - Validation temporelle (Date de départ > Date d'arrivée).

### 🌐 FrontOffice (Site Public)
- **Catalogue :** Liste des chambres disponibles accessible à tous.
- **Interface :** Tableau clair et lisible.
- **Tri Intelligent :** Les chambres sont automatiquement triées par capacité croissante pour faciliter le choix.

---

## 🏗️ Architecture Technique

Le projet est construit sur une architecture modulaire Django avec 3 applications distinctes :

| Application | Rôle | Modèles Principaux |
|-------------|------|--------------------|
| **ClientApp** | Gestion des utilisateurs et authentification | `Client` (étend AbstractUser) |
| **CategoryApp** | Gestion de la taxonomie des chambres | `Category` |
| **RoomApp** | Cœur du métier (Chambres, Réservations) | `Room`, `Reservation` |

### Technologies
- **Backend :** Python, Django
- **Base de données :** SQLite (Par défaut), compatible PostgreSQL/MySQL
- **Frontend :** HTML5, CSS3, Django Templates

---

## 🛠️ Installation et Démarrage

Suivez ces étapes pour lancer le projet localement.

### Prérequis
- Python 3.8 ou supérieur
- Git

### 1. Cloner le dépôt
```bash
git clone https://github.com/AbdelhafidhGHARBI/gestion-hotel-django.git
cd gestion-hotel-django
```

### 2. Créer l'environnement virtuel
Il est recommandé d'utiliser un environnement virtuel pour isoler les dépendances.

**Sous Windows :**
```bash
python -m venv venv
.\venv\Scripts\activate
```

**Sous macOS / Linux :**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Installer les dépendances
```bash
pip install django
```

### 4. Configurer la base de données
Appliquez les migrations pour créer la structure de la base de données.
```bash
python manage.py migrate
```

### 5. Créer un administrateur
Pour accéder au BackOffice, créez un superutilisateur.
```bash
python manage.py createsuperuser
# Email obligatoire : doit finir par @gmail.com
```

### 6. Lancer le serveur
```bash
python manage.py runserver
```
- **FrontOffice :** http://127.0.0.1:8000/
- **BackOffice :** http://127.0.0.1:8000/admin/

---

## 🔒 Règles de Validation

Le système applique des règles strictes pour garantir l'intégrité des données :

1.  **Chambres (`room_number`)**
    - Doit commencer par "Room", suivi d'une lettre et de chiffres.
    - *Exemple Valide :* `RoomA101`, `RoomB20`.
    - *Exemple Invalide :* `101`, `Chambre1`.

2.  **Clients (`email`)**
    - L'email doit être unique.
    - Seuls les emails Google (`@gmail.com`) sont acceptés.

3.  **Catégories (`category_name`)**
    - Longueur comprise entre 10 et 100 caractères.

4.  **Réservations**
    - La date de check-in doit être aujourd'hui ou dans le futur.
    - La date de check-out doit être strictement postérieure au check-in.

---

## 👤 Auteur

**Abdelhafidh GHARBI**
- GitHub : [AbdelhafidhGHARBI](https://github.com/AbdelhafidhGHARBI)

---
*Projet réalisé avec Django - 2026*
