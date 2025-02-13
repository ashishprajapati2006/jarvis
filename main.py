import speech_recognition as sr
import webbrowser
import pyttsx3
import google.generativeai as genai
import requests
import os
import musicLibrary
import pygame
from gtts import gTTS

# Configure Gemini AI
genai.configure(api_key="AIzaSyCvGIIAJAW43kdC2x0EUAU_6q9tFmNSxdw")
model = genai.GenerativeModel("gemini-pro")

# Initialize recognizer and engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "dcf7efab62494845b32e5cdcf5dba535"

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')
    pygame.mixer.init()
    pygame.mixer.music.load('temp.mp3')
    pygame.mixer.music.play()
    
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.unload()
    os.remove("temp.mp3")

def ai_process(command):
    response = model.generate_content(command)
    return response.text.strip() if response.text else "Sorry, I couldn't understand that."

def get_news():
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey=dcf7efab62494845b32e5cdcf5dba535"
    try:
        data = requests.get(url).json()
        articles = data.get("articles", [])
        return [article["title"] for article in articles[:3]] 
    except:
        return ["Unable to fetch news."]

def process_command(command):
    command = command.lower()
    
    commands = {
        "open google": "https://google.com",
        "open facebook": "https://facebook.com",
        "open youtube": "https://youtube.com",
        "open linkedin": "https://linkedin.com"
    }
    
    if command in commands:
        webbrowser.open(commands[command])
    elif "news" in command:
        for news in get_news():
            speak(news)
    elif command.startswith("play"):
        song = command.split(" ", 1)[1]
        link = musicLibrary.music.get(song, None)
        if link:
            webbrowser.open(link)
        else:
            speak("Song not found in library.")
    else:
        speak(ai_process(command))

def listen():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening for 'Jarvis'...")
        while True:
            try:
                audio = recognizer.listen(source, timeout=5)
                wake_word = recognizer.recognize_google(audio).lower()
                if wake_word == "jarvis":
                    speak("Yes?")
                    break
            except sr.UnknownValueError:
                continue
            except Exception as e:
                print("Error:", e)
        
        print("Jarvis Activated...")
        while True:
            try:
                audio = recognizer.listen(source)
                command = recognizer.recognize_google(audio)
                process_command(command)
            except sr.UnknownValueError:
                continue  # Ignore unrecognized speech
            except Exception as e:
                print("Error:", e)

if __name__ == "__main__":
    speak("Initializing Jarvis...")
    listen()
