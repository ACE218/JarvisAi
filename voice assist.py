import subprocess
import wolframalpha
import pyttsx3
import random
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import cv2
import pyjokes
import pywhatkit as kit
import datetime 
import json
from requests import get
import tkinter 
from tkinter import *
import shutil
import psutil
import points
import datetime


voiceEngine = pyttsx3.init('sapi5')
voices = voiceEngine.getProperty('voices')
voiceEngine.setProperty('voice', voices[0].id)

def speak(text):
	voiceEngine.say(text)
	voiceEngine.runAndWait()

def wish():
    print("Wishing.")
    time = int(datetime.datetime.now().hour)
    global uname,asname
    if time>= 0 and time<12:
        speak("Good Morning sir ")

    elif time<18:
        speak("Good Afternoon sir ")

    else:
        speak("Good Evening sir ")

    asname ="Jarvis"
    speak("I am your Voice Assistant,")
    speak(asname)
    print("I am your Voice Assistant,",asname)
def getName():
    global uname
    speak("Can I please know your name?")
    uname = takeCommand()
    print("Name:",uname)
    speak("Thank you for told me your name ")
    columns = shutil.get_terminal_size().columns
    speak("How can i Help you, ")
    speak(uname)

def takeCommand():
    global showCommand
    showCommand.set("Listening....")
    cmdLabel.config(textvariable=points)

    recog = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening to the user")
        recog.pause_threshold = 1
        userInput = recog.listen(source)

    try:
        print("Recognizing the command")
        command = recog.recognize_google(userInput, language ='en-in')
        print(f"Command is: {command}\n")

    except Exception as e:
        print(e)
        #print("Unable to Recognize the voice.")
        return "None"

    return command



def getWeather(cityName):
    cityName=takeCommand() 
    baseUrl = "http://api.openweathermap.org/data/2.5/weather?" 
    url = baseUrl + "appid=" + '4b784d5ef42f0ff19e9d1938ac8e00ca' + "&q=" + cityName  
    response = get(url)
    x = response.json()

    #If there is no error, getting all the weather conditions
    if x["cod"] != "404":
        y = x["main"]
        temp = y["temp"]
        temp-=273 
        pressure = y["pressure"]
        humidiy = y["humidity"]
        desc = x["weather"]
        #description = y[0]["description"]
        info=(" Temperature= " +str(temp)+"°C"+"\n atmospheric pressure (hPa) ="+str(pressure) +"\n humidity = " +str(humidiy)+"%" )
        print(info)
        speak("Here is the weather report at")
        speak(cityName)
        speak(info)
    else:
        speak(" City Not Found ")

def jokes():
    my_joke = pyjokes.get_joke('en',category='neutral')
    print(my_joke)
    speak(my_joke)

def news():
    main_url = 'https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=4f9b8cee4f4744258194e210663b2661'
    
    main_page = get(main_url).json()
    articles = main_page["articles"]
    
    head = []
    day=["first","second","third"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        speak(f"today's {day[i]} news is: {head[i]}")  
    
def callVoiceAssistant():

    uname=''
    asname=''
    os.system('cls')
    wish()
    getName()
    print(uname)

    while True:

        command = takeCommand().lower()
        print(command)

        if "jarvis" in command:
            wish()
            
        elif "open notepad" in command:
           speak("notepad is opening\n sir")
           npath = "C:\\Windows\\System32\\notepad.exe"
           os.startfile(npath)
           
        elif "what is my ip address" in command:
           ip = get('https://api.ipify.org').text
           speak(f"your Ip address is{ip}")
           
        elif "open command prompt" in command:
           speak(" opening command prompt\n sir")
           os.system("start cmd")
           
        elif "open camera" in command:
           speak("opening camera\n sir")
           cap = cv2.VideoCapture(0)
           while True:
               ret, img =cap.read()
               cv2.imshow('webcam', img)
               k = cv2.waitKey(50)
               if k==27:
                   break;
           cap.release()
           cv2.destroyAllWindows()        
        
        elif 'time' in command:
            strTime = datetime.datetime.now()
            curTime=str(strTime.hour)+"hours"+str(strTime.minute)+"minutes"+str(strTime.second)+"seconds"
            speak(uname)
            speak(f" the time is {curTime}")
            print(curTime)
            
        
        elif 'wikipedia' in command:
            speak('Searching Wikipedia')
            command = command.replace("wikipedia", "")
            results = wikipedia.summary(command, sentences = 2)
            speak("These are the results from Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in command:
            speak(" Youtube is opening\n sir")
            webbrowser.open("www.youtube.com")

        elif 'open google' in command:
            speak("Opening Google\n sir")
            webbrowser.open("www.google.com")
            
        elif 'open facebook' in command:
            speak("opening facebook\n sir") 
            webbrowser.open("www.facebook.com")
            
        elif 'open instagram' in command:
            speak("opening instagram\n sir")
            webbrowser.open("www.instagram.com")       

        elif 'play music' in command or "play song" in command:
            speak("Enjoy the music!")
            music_dir = "D:\\Music1"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
            

        elif 'tell me a joke' in command:
            jokes()
            

        elif 'exit' in command:
            speak("Thank you sir ,for giving me your time")
            exit()

        
        elif "weather" in command:
            speak(" Please tell your city name ")
            print("City name : ")
            cityName = takeCommand()
            getWeather(cityName)

        elif "what is" in command or "who is" in command:
            
            client = wolframalpha.Client("UJXPPY-378TH3L8AJ")
            res = client.query(command)

            try:
                print (next(res.results).text)
                speak (next(res.results).text)
            except StopIteration:
                print ("No results")

        elif 'search' in command:
            command = command.replace("search", "")
            webbrowser.open(command)

        elif "tell me a news" in command:
           speak("please wait sir,fetching the latest news")
           news()  
           
        elif "how much battery left" in command:
            battery = psutil.sensors_battery()
            percentage = battery.percent
            speak(f"sir our system have {percentage} percent battery")
  
        
        elif 'shutdown system' in command:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown / p /f')

        elif "restart" in command:
            subprocess.call(["shutdown", "/r"])

        elif "sleep" in command:
            speak("Setting in sleep mode")
            subprocess.call("shutdown / h")

        

#Creating the front page of jarvis
#Creating the main window 
wn = tkinter.Tk() 
wn.title("Jarvis Voice Assistant")
wn.geometry('700x300')
wn.config(bg='LightBlue1')
  
Label(wn, text='Welcome to meet the Voice Assistant by Jarvis', bg='LightBlue1',
      fg='black', font=('Courier', 30)).place(x=50, y=30)


Button(wn, text="Start", bg='green',font=('Courier', 18),
       command=callVoiceAssistant).place(x=500, y=200)

showCommand=StringVar()
cmdLabel=Label(wn, textvariable=showCommand, bg='LightBlue1',
      fg='black', font=('Courier', 15))
cmdLabel.place(x=250, y=150)

#Runs the window till it is closed
wn.mainloop()