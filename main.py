import speech_recognition as sr

listner = sr.Recognizer()

try:
    with sr.Microphone() as source:
        voice = listner.listen(source)
except:
    pass