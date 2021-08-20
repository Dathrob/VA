import speech_recognition as sr
import pyttsx3
from googletrans import Translator, constants
import pywhatkit
translator = Translator()

listner = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('rate', 100)

try:
    with sr.Microphone() as source:
       
       
        print("listning")
        voice = listner.listen(source)
        command = listner.recognize_google(voice,language="am-ET")
        translation = translator.translate(command)
        t_command = translation.text
        #engine.say(t_command)
        #engine.runAndWait()
        print(command)
        pywhatkit.playonyt(t_command)
        
except:
    print("mic is not working")
    