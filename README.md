# 🌡️ Convertisseur de Température - Django

## 📝 Description

Ce projet est une **application web développée avec Django** permettant :
- D'ajouter un utilisateur
- De convertir des températures** entre Celsius, Fahrenheit et Kelvin, associées à un utilisateur
- De voir l'historique des conversions** de chaque utilisateur

L'application utilise **Django, Bootstrap** pour le style et une base de données pour stocker les conversions et les utilisateurs.

---

## 🎯 Fonctionnalités

✔️ **Ajout d'un utilisateur avant toute conversion**  
✔️ **Sélection de l'utilisateur pour effectuer une conversion**  
✔️ **Conversion entre Celsius, Fahrenheit et Kelvin**    
✔️ **Consultation de l'historique des conversions**  
✔️ **Interface simple et responsive (Bootstrap)**  
✔️ **Gestion des super-utilisateurs pour l’administration**  

---

## 📸 Captures d’écran

### 🌍 Page principale : Sélection et conversion
![Homepage](screenshots/homepage.png)

### 🔥 Résultat d'une conversion
![Conversion Example](screenshots/conversion.png)

### 📜 Historique des conversions d'un utilisateur
![Historique](screenshots/historique.png)

*(Ajoute ces images dans un dossier `/screenshots` dans ton repo pour qu’elles s'affichent correctement.)*

---

## 🚀 Installation et Exécution
- Creation d'un environnement virtuel sur windows :
``` sh
python -m venv .venv
.venv\Scripts\activate
```

Dans votre environnement virtuel, exécutez ces commandes pour installer les dépendances nécessaires :

```sh
pip install django
pip install django-bootstrap4
```
Apres ca on applique les migrations :

```sh
python manage.py makemigrations
python manage.py migrate
```
Et enfin on lance le serveur 
```sh
python manage.py runserver 8001





