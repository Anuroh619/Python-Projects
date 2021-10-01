'''
Author - Anay Gour
Date - 01 Oct 2021
Purpose - Project for python
Title - Iron Man Jarvis Desktop Voice Assistant
'''
import pyttsx3 # pip install pyttsx3
import datetime
import speech_recognition as sr # pip install SpeechRecognition

def speak(audio):
    '''
    This function will take an string as an input and will speak that string.
    '''
    engine = pyttsx3.init('sapi5')
    voice = engine.getProperty('voices')
    engine.setProperty('voice', voice[0].id)
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():
    '''
    This function will wish accoriding to time.
    '''
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("Good Morning!")

    elif hour >= 12 and hour <= 15:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis. How can I help you?")
    
if __name__ == '__main__':
    wishMe()
