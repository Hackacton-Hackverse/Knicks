<h1 align="center">Knicks Todo App For Hackverse </h1>


## Table of Contents
- [Previsualisation](#previsualilsation)
- [Pile Technologique](#tech_stack)
- [Installation](#installation)
- [Fonctionnalités](#features)

# 💻 Pile Technologique :
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)

# Previsualilsation : 

![Welcome_first](/tuto/welcome_first.png)
![inscription](/tuto/inscription.png)
![connexion](/tuto/connexion.png)
![Welcome](/tuto/welcome.png)
![Create Task](/tuto/create_task.png)
![Views Task](/tuto/view_task.png)
![Category](/tuto/category.png)
![Profile](/tuto/profile.png)

## Installation

### Clôner le dépot Gitt

Pour commencer avec l'application Knicks Todo App, vous pouvez cloner le dépôt depuis GitHub de l'organisation Hackverse si vous y êtes membre en suivant les étapes suivantes
1. **Clone the repository**:

   ```bash
   git clone https://github.com/
   
2. Navigate to the project folder:
   ```bash
   cd Todo_List
   
3. Créez et activez un environnement virtuel (facultatif mais recommandé):
   ```bash
   py -m venv env
   myworld\Scripts\activate.bat
   
4. Installer les dépendances du projet:
   ```bash
   pip install -r requirements.txt
   
5. Lancer les migrations vers la base de données SQLITE 3 :
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   
7. Creer un superutilisateur pour les accès administrateurs : 
   ```bash
   python manage.py createsuperuser
   
8. Lancer le serveur de developement  : 
   ```bash
   python manage.py runserver
   

## Fonctionnalités

L'application web Knicks Todo App offre les fonctionnalités suivantes :

- **Gestion des tâches** : Ajoutez, modifiez et supprimez facilement des tâches.
- **Priorisation des tâches** : Attribuez des niveaux de priorité aux tâches.
- **Catégorisation des tâches** : Divisez les tâches en différentes catégories.
- **Authentification des utilisateurs** : Gestion sécurisée des comptes.
- **Tableau de bord de l'administrateur** : Accédez au tableau de bord de l'administrateur [http://localhost:8000/admin/](http://localhost:8000/admin/) pour gérer les utilisateurs et les tâches.
- **Gestion du profil** : Modifiez les détails de l'utilisateur (photo, e-mail, mot de passe, nom, etc.).
- **Exportation des détails des tâches** : Téléchargez un fichier PDF / CSV de vos tâches.