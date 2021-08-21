import speech_recognition as sr
import pyttsx3
from googletrans import Translator, constants
import pywhatkit
import os
from playsound import playsound
translator = Translator()
listner = sr.Recognizer()
engine = pyttsx3.init()
playsound('synthesize.mp3')
def searcher(query):
    print("search is called")
    pywhatkit.search(query)
    starter()



def open(application):
    print("open is called")
    engine.say("opening"+application)
    engine.runAndWait()
    os.system(application)
    starter()



def youtube(item):
    pywhatkit.playonyt(item)



def starter():
    try:
        with sr.Microphone() as source:
            print("listning")
            voice = listner.listen(source,phrase_time_limit=4)
            command = listner.recognize_google(voice,language="am-ET")
            print(command)
            if(("ቪዲዮ" in command)or("video" in command)):
                print("video found")
                query = command.replace("ቪዲዮ","")
                youtube(command)
            elif(("ፍለጋ" in command) or ("በመፈለግ ላይ" in command) or ("ፈልግ" in command)):
                query = command.replace("ፈልግ"," ")
                searcher(command)
            elif(("ክፈት" in command) or ("ክፍት" in command) or ("ከፈተልኝ" in command) or("ከፍ ሲል" in command)):
                application = command.replace("ክፈት","")
                application = command.replace("ክፍት","")
                application = command.replace("ከፈተልኝ","")
                application = command.replace("ከፍ ሲል","")
                translation = translator.translate(application)
                open_command = translation.text
                open(open_command)
            else:
                playsound('synthesize (1).mp3')
                starter()
            
        
    except:
        engine.say("sorry command not found")

starter()

