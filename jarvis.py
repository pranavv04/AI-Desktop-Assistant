from email.mime import audio
from pip import main
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
# import os
import random
import cv2
import pywhatkit as kit
import sys
import pyautogui
import time
import operator
import requests



engine=pyttsx3.init('sapi5')# for voices use sapi5 google it
voices=engine.getProperty('voices')
# print(voices[0].id) #use 0 for male voice and use 1 for female voice
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour > 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 17:
        speak("Good Afternoon")
    elif hour >= 17 and hour < 19:
        speak("Good Evening")
    elif hour >= 19 and hour < 24:
        speak("Good Night")

    speak("I your Assistant Sir  Please tell me how may i help you")


def takeCommand():
    # it takes microphone input from user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1  # time taken to close if you stop speaking
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f"User said :{query}")
        
    except Exception as e:
        #  print(e)
        print("Say that again please")
        return 'None'
    return query 

if __name__ == '__main__':
    wishMe()
    while True:
     query=takeCommand().lower()
    
    #logic for executing task
     if 'wikipedia' in query:
         speak('Searching wikipedia...')
         query = query.replace("wikipedia","")
         results = wikipedia.summary(query,sentences =2)
         speak("According to Wikipedia")
         print(results)
         speak(results)
     elif 'open youtube' in query:
        #   webbrowser.open("youtube.com")
          chromepath = 'C://Program Files (x86)//Google//Chrome//Application//chrome.exe %s'
          webbrowser.get(chromepath).open_new_tab('youtube.com')
         
     elif 'open google' in query:
        #  webbrowser.open("google.com")
         chromepath = 'C://Program Files (x86)//Google//Chrome//Application//chrome.exe %s'
         webbrowser.get(chromepath).open_new_tab('google.com')
         
     elif 'open stack overflow' in query:
        #  webbrowser.open("stackoverflow.com")
         chromepath = 'C://Program Files (x86)//Google//Chrome//Application//chrome.exe %s'
         webbrowser.get(chromepath).open_new_tab('stackoverflow.com')
         
     elif 'search in chrome' in query:
         speak('what should i search for')
         search=takeCommand()
         chromepath = 'C://Program Files (x86)//Google//Chrome//Application//chrome.exe %s'
         webbrowser.get(chromepath).open_new_tab(search+'.com')
     elif 'open spotify' in query:
         speak('which song should i play')
         search=takeCommand()
         spotifypath = 'C://Users//User//AppData//Roaming//Spotify//spotify.exe %s'
         webbrowser.get(spotifypath).open_new(search+'song')
         #spotify.exe= os.listdir(spotifypath)
        # os.startfile(os.path.join(spotifypath,[0]))
     elif 'search on youtube' in query:
         query = query.replace("search on youtube", "")
         webbrowser.open(f"www.youtube.com/results?search_query={query}")     
     elif 'close chrome' in query:
         os.system("taskkill /f /im chrome.exe")
     elif 'close youtube' in query:
         os.system("taskkill /f /im msedge.exe")
     elif 'the time' in query:
         strTime = datetime.datetime.now().strftime("%H:%M:%S")
         speak(f"Sir, the time is {strTime}")
     elif "shut down the system" in query:
         os.system("shutdown /s /t 5")
     elif "restart the system" in query:
         os.system("shutdown /r /t 5")
     elif "Lock the system" in query:
         os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")    
     elif "open notepad" in query:
         npath = "C:\Windows\system32\notepad"
         os.startfile(npath)
     elif "close notepad" in query:
         os.system("taskkill /f /im notepad.exe")
     elif "open command prompt" in query:
         os.system("start cmd")

     elif "close command prompt" in query:
          os.system("taskkill /f /im cmd.exe")

     elif "go to sleep" in query:
       speak(' alright then, I am switching off')
       sys.exit()

     elif "take screenshot" in query:
        speak('tell me a name for the file')
        name = takeCommand().lower()
        time.sleep(3)
        img = pyautogui.screenshot()
        img.save(f"{name}.png")
        speak("screenshot saved")

     elif "what is my IP address" in query:
        speak("Checking")
     try:
       ipAdd = requests.get('https://api.ipify.org').text
       print(ipAdd)
       speak("your ip adress is")
       speak(ipAdd)
     except Exception as e:
       speak("network is weak, please try again some time later")
