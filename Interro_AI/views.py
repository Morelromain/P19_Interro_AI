import os
import pyautogui
import pytesseract
from PIL import Image
import openai
import win32gui

from django.shortcuts import render
from .utils import screen_printer, image_conversion, use_brain


def home_view(request):
    debut_question = request.POST.get('debut_question')
    # fin_question = request.POST.get('fin_question')
    question = ''
    reponse = ''
    if debut_question is None : debut_question = ''
    # if fin_question is None : fin_question = ''
    screen_printer()
    if debut_question != '':
        question = image_conversion(debut_question)
    if "Echec de la selection du texte," not in question and debut_question != '':
        reponse = use_brain(question)
    return render(
        request, 
        'home.html', 
        {
            'debut_question': debut_question, 
            'question': question, 
            'reponse': reponse
        }
        )

def link_view(request):
    return render(request, 'link.html')
