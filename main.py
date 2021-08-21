import speech_recognition as sr
import pyttsx3
from googletrans import Translator, constants
import pywhatkit
import os
from playsound import playsound
translator = Translator()
listner = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('rate', 120)
#engine.say("Hello  misganaw  how  can  i  help  you")
#engine.runAndWait()
playsound('synthesize.mp3')
def search(query):
    pywhatkit.search(query)
    starter()
def open(application):
    engine.say("opening"+application)
    engine.runAndWait()
    os.system(application)
    starter()
    
def starter():
    try:
        with sr.Microphone() as source:
           
            print("listning")
            voice = listner.listen(source,phrase_time_limit=4)
            command = listner.recognize_google(voice,language="am-ET")
            print(command)

            if("ክፈት" or "ክፍት" or "ከፈተልኝ" or"ከፍ ሲል" in command):
                application = command.replace("ክፈት","")
                application = command.replace("ክፍት","")
                application = command.replace("ከፈተልኝ","")
                application = command.replace("ከፍ ሲል","")
                translation = translator.translate(application)
                open_command = translation.text
                print("translated"+open_command)
                open(open_command)
            elif("ፍለጋ" or"በመፈለግ ላይ" or "ፈልግ" in command ):
                query = command.replace("ፈልግ"," ")
                translation = translator.translate(query)
                t_command = translation.text
                search(t_command)
            elif("ቪዲዮ" in command):
                translation = translator.translate(command)
                t_command = translation.text
                query = command.replace("ቪዲዮ","")
                
            else:
                engine.say("sorry the command is unkown")
                starter()
            #pywhatkit.playonyt(t_command)
        
    except:
        print("mic is not working")

starter()