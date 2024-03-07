import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
 
import smtplib
import openai
from config import apikey


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)
chatStr = ""
# https://youtu.be/Z3ZAJoi4x6Q
def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = apikey
    chatStr += f"Biswa: {query}\n Jarvis: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
def ai(prompt):
    openai.api_key = apikey
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"

    response = openai.Completion.create(
    model="text-davinci-004",  # Replace with the appropriate model name
    prompt=chatStr,
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

    # todo: Wrap this inside of a  try catch block
    # print(response["choices"][0]["text"])
    text += response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    # with open(f"Openai/prompt- {random.randint(1, 2343434356)}", "w") as f:
    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip() }.txt", "w") as f:
        f.write(text)

def say(text):
    os.system(f'say "{text}"')

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")

    elif 12 <= hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak(" greetingss   master I am friday yor personal Ai assistant, I am a new version of jaaarvis . Please tell me how may I help you ")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if "play music" in query:
            webbrowser.open("youtube.com/watch?v=9-Vc4xmTZKk")
        elif "play nattu nattu" in query:
            webbrowser.open("youtube.com/watch?v=OsU0CGZoV8E")
        elif "the time" in query:
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            speak(f"Sir time is {hour} baaajjke {min} minutes")

        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'open insta' in query:
            webbrowser.open("instagram.com")
        
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif "open word".lower() in query.lower():
            os.system(r"start winword")

        elif "open powerpoint".lower() in query.lower():
            os.system(r"start powerpnt")

        elif "open camera".lower() in query.lower():
            os.system(r"start microsoft.windowscamera:")

        elif "Using artificial intelligence".lower() in query.lower():
            ai(prompt=query)

        elif 'email to biswajit' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "biswajitbauri21803@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend biswa bhai. I am not able to send this email")

        elif "Friday Quit".lower() in query.lower():
            exit()

        elif "reset chat".lower() in query.lower():
            chatStr = ""

        elif 'Viswajeet' in query:
                speak("yes my master")
                webbrowser.open("instagram.com/_ig_biswa_")

        elif 'mihir' in query:
                speak("GREETINGS")
                webbrowser.open("instagram.com/ig_m_ihi_r_x")


        elif 'rishab' in query:
                speak("GREETINGS")
                webbrowser.open("instagram.com/rishavgoenkaa")

        elif 'suman' in query:
                speak("GREETINGS")
                webbrowser.open("instagram.com/suman_das_0910")
        
        elif 'who is your daddy' in query:
                speak("Khokababu")
        
        
