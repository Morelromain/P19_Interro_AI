import os
import pyautogui
import pytesseract
import openai
import win32gui
from PIL import Image
import configparser 
import win32api

from .settings import AI_KEY

def screen_printer(): 
    if not os.path.exists("captures"):
        os.makedirs("captures")
    screen_width, screen_height = pyautogui.size()
    capture_width = screen_width // 2
    capture_height = screen_height
    capture_left = screen_width // 2
    capture_top = 0
    capture = pyautogui.screenshot(region=(capture_left, capture_top, capture_width, capture_height))
    capture.save("captures/capture.png")

def image_conversion(debut_question):
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'
    image = Image.open("captures/capture.png")
    texte_total = pytesseract.image_to_string(image)
    try :
        debut_index = texte_total.index(debut_question)
        texte_coupe = texte_total[debut_index:]
        fin_index = texte_coupe.index('\n\n')
        partie_texte = texte_total[debut_index:debut_index+fin_index]
        question = f"La question : {partie_texte}"
    except Exception:
        question = f"Echec de la selection du texte, voici tout le texte trouvé de la capture : \n {texte_total}\n"
    return question

def use_brain(question):
    try:
        openai.api_key = AI_KEY
        precision = ("Réponds à la question suivante : \n")
        prompt = f"{precision} {question}"
        completion = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=1024,
            n=1,
        stop=None,
            temperature=0.5,
        )
        reponse = completion.choices[0].text
        reponse = f"La réponse : {reponse}"
    except Exception as e:
        reponse = "Openai actuellement HS, veuillez réessayer un peu plus tard :"
    return reponse
