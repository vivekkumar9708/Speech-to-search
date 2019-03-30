import speech_recognition as sr
import webbrowser as wb
import pyttsx3

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

r = sr.Recognizer()

with sr.Microphone() as source:
    print ('Say Something sir!')
    audio = r.listen(source)
    print ('wait a second.....! I am searching...')
 
try:
    text = r.recognize_google(audio)
    print('Google thinks you said:\n' + text)
    
    f_text = 'https://www.google.co.in/search?q=' + text
    wb.get(chrome_path).open(f_text)


    text_speech = pyttsx.init('sapi5')
    text_speech.setProperty('rate', 150)


 
except Exception as e:
    print (e)
