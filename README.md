# Interro_AI

Django application for AI-assisted online examination/quiz assistance.  

[Readme in French](#français)  

Warning: Cheating is bad! This application was made with the sole purpose of highlighting the weaknesses of online exams.  

![<exemple>](https://github.com/Morelromain/P19_Interro_AI/blob/main/captures/exemple.png)

## Functionality

This application allows for answering questions on an online exam/quiz.  
- Even if the questions are in image format, the text will still be converted and extracted.
- The answer will be given within a few seconds.

Steps to follow:  
- Step 1: Press Windows + left arrow to put the application page on the left side and the web page/exam document on the right side.
- Step 2: Enter the first word of the question.
- Step 3: Click on Submit.

Note:

- The text of the question must be readable and not too small, do not hesitate to zoom in on the question.
- The answers are generated using OpenAI, the system is not infallible and may make mistakes.

## Installation:

Python version: 3.8.3 minimum  
Detailed installation for Windows system.  

- Install Tesseract on your computer:
`[https://github.com/UB-Mannheim/tesseract/wiki]`(https://github.com/UB-Mannheim/tesseract/wiki)  

- Sign up for OpenAI, then retrieve your api_key_AI:
`[https://beta.openai.com/account/api-keys]`(https://beta.openai.com/account/api-keys)  

- Clone this code repository using the command:
`$ git clone https://github.com/Morelromain/Interro_AI.git`  

- Go to the root of the Interro_AI directory using the command:
`$ cd Interro_AI`  

- Create a virtual environment for the project:
`$ python -m venv env`  

- Install the project dependencies with the command:
`$ pip install -r requirements.txt`  

In the Interro_AI\settings.py file, enter your api_key_AI in the `AI_KEY` variable (line 25)

## Execution

- Activate the virtual environment:
`$ env\Scripts\activate`

- Start the server with `$ python manage.py runserver`

To access the application: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

*[Documentation Django](https://docs.djangoproject.com/en/4.1/)*

---

<a name="français"></a>*En Français*

Application Django d'assistance aux examens/quizz en ligne par intelligence Artificielle.  

Avertissement : Tricher, c'est mal! Cette Application a été faite dans l'unique but de mettre en avant les faiblesses des examens en lignes.

![<exemple>](https://github.com/Morelromain/P19_Interro_AI/blob/main/captures/exemple.png)

## Fonctionnement

Cette application permet de répondre aux questions d'un examen/quizz en ligne.  
- Même si les questions sont au format d'image, le texte sera quand même converti et extrait.  
- La réponse sera donnée en quelques secondes.  

Les étapes à suivres :  
- Etape 1 : Appuyez sur Windows + flèche gauche pour mettre la page de l'application sur le coté gauche, et la page web/le document de l'examen sur le coté droit.   
- Etape 2 : Rentre le premier mot de la question.  
- Etape 3 : Clique sur Envoyer.  

Important :  
- Le texte de la question doit être lisible et pas trop petit, ne pas hésiter à zoomer sur la question.
- Les réponses sont générées grace à open_AI, le système n'est pas infaillible et peut se tromper.  

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

*[Documentation Django](https://docs.djangoproject.com/fr/4.1/)*
