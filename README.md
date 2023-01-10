# Interro_AI

Application Django d'assistance aux examens/quizz en ligne par intelligence Artificielle.  

## Fonctionnement

Cette application permet de répondre aux questions d'un examen/quizz en ligne.  
- La question peut-être sous un format sécurisé d'image, le texte sera quand même extrait.  
- La réponse sera donné en quelques secondes.  

Les étapes à suivres :  
- Etape 1 : Appuye sur Windows + flèche gauche pour mettre cette page web sur le coté gauche, et la page web/document de ton examen sur le coté droit.  
- Etape 2 : Dans ton test, zoom sur la question de ton choix avec Controle + Molette avant.  
- Etape 3 : Rentre le premier mot et le dernier mot de la question.  
- Etape 4 : Clique sur Envoyer.  

Attention :  
- Les réponses sont générées grace à open_AI, le système n'est pas infaillible et peut se tromper.  
- Tricher, c'est mal, cette Application a été faite dans le but de mettre en avant certaines faiblesses des examens en lignes.

![<exemple>](https://github.com/Morelromain/P19_Interro_AI/blob/main/captures/exemple.png

## Installation

Version Python : 3.8.3 minimum  
Installation détaillé pour système Windows.  

- Installez Tesseract sur votre ordinateur (lors de l'installation, selectionner "français") :  
`[https://github.com/UB-Mannheim/tesseract/wiki]`(https://github.com/UB-Mannheim/tesseract/wiki)  

- Inscrivez-vous à OpenAI, puis récupérez votre api_key_AI :  
`[https://beta.openai.com/account/api-keys]`(https://beta.openai.com/account/api-keys)  

- Clonez ce dépôt de code à l'aide de la commande :  
`$ git clone https://github.com/Morelromain/Interro_AI.git`  

- Rendez-vous depuis un terminal à la racine du répertoire Interro_AI avec la commande :  
`$ cd Interro_AI`  

- Créez un environnement virtuel pour le projet :  
`$ python -m venv env`  

- Installez les dépendances du projet avec la commande :  
`$ pip install -r requirements.txt`  

- Dans le fichier `Interro_AI\settings.py` rentrez votre api_key_AI dans la variable `AI_KEY` (ligne 25)  

## Exécution

- Activez l'environnement virtuel :  
`$ env\Scripts\activate`

- Démarrez le serveur avec `$ python manage.py runserver`

Pour accéder à l'application : [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

*[Documentation Django](https://docs.djangoproject.com/fr/3.1/)*
