import speech_recognition as sr
import pyttsx3
from googletrans import Translator, constants
import pywhatkit
translator = Translator()

listner = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('rate', 100)

def search(query):
    pywhatkit.search(query)
try:
    with sr.Microphone() as source:
        print("listning")
        voice = listner.listen(source,phrase_time_limit=4)
        command = "ኣቢይ ኣህመድ ፈልግ"
        #command = listner.recognize_google(voice,language="am-ET")
       
        #engine.say(t_command)
        #engine.runAndWait()
        print(command)
        
        if("ፍለጋ" or"በመፈለግ ላይ" or "ፈልግ" in command ):
            query = command.replace("ፈልግ"," ")
            translation = translator.translate(query)
            t_command = translation.text
            search(t_command)
        if("ቪዲዮ" in command):
            translation = translator.translate(command)
            t_command = translation.text
            query = command.replace("ቪዲዮ","")
            pywhatkit.playonyt()
        #pywhatkit.playonyt(t_command)
        
except:
    print("mic is not working")


