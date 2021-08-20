import speech_recognition as sr
import pyttsx3
from googletrans import Translator, constants

listner = sr.Recognizer()
engine = pyttsx3.init()  

try:
    with sr.Microphone() as source:
        print("listning")
        voice = listner.listen(source)
        command = listner.recognize_google(voice,language="am-ET")

        engine.say(command)
        engine.runAndWait()
        print(command)
except:
    print("mic is not working")
    