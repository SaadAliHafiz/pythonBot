import pyttsx3
import os
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import random
#import wolframalpha
#import mysql.connector as con
#import ezgmail
import pyautogui
#import pygame
#from nltk.chat.util import Chat, reflections
#from PIL import ImageTk,Image
from tkinter import *

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hr = int(datetime.datetime.now().hour)
    if hr >= 0 and hr < 12:
        speak("good morning")
    elif hr >= 12 and hr < 18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("hi my name is pandora i am your digital assistant")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        print("recognizing...")
        query = r.recognize_google(audio,language = "en-in")
        print(f"user said:{query}\n")
    except Exception as e:
        speak("sorry sir i did not got that")
        print(e)
        query = pyautogui.prompt("commmand:")
    return query
takecommand()