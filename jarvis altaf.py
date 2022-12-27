# personal assistant


import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')  # getting details of current voice

engine.setProperty('voice', voices[1].id)


def speak(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()


def wish_me():
    hours = int(datetime.datetime.now().hour)
    if 0 <= hours < 12:
        speak("Good morning!")
    elif 12 <= hours <= 16:
        speak("Good afternoon!")
    elif 16 < hours <= 19:
        speak("Good evening")
    elif 19 < hours <= 23:
        speak("Good night my dear")


def take_command():
    recognize = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        recognize.pause_threshold = 1
        audio = recognize.listen(source)
    try:
        print("Recognizing...")
        query = recognize.recognize_google(audio, language='en-in')  # Using google for voice recognition.
        print(f"User said: {query}\n")  # User query will be printed.

    except Exception as e:
        # print(e)
        print("Say that again please...")  # Say that again will be printed in case of improper voice
        return "None"  # None string will be returned
    return query


def send_emails(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('eraltaf688@gmail.com', 'altaf688@')
    server.sendmail('eraltaf688@gmail.com', to, content)
    server.close()


if __name__ == '__main__':
    wish_me()
    speak("Hello! I am Jarvis. Your personal assistant, How may I help you simran urf gudiya")
    while True:
        query = take_command().lower()  # Converting user query into lower case

        # Logic for executing tasks based on query
        if 'wikipedia' in query:  # if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            print(query)
            query = query.replace("wikipedia", "")
            print(query)
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'youtube' in query:
            print(query)
            speak("opening youtube")
            webbrowser.open('youtube.com')

        elif 'google' in query:
            print(query)
            speak('opening google')
            url = 'https://www.google.com'
            webbrowser.open_new(url)

        elif 'stop' in query:
            print(query)
            speak("I am happy to help you. we are going to exit  simran urf gudiya")
            exit()

        elif 'whatsapp' in query:
            print(query)
            speak("opening whatsapp")
            os.startfile('C:\\Users\\Altaf khan\\AppData\\Local\\WhatsApp\\WhatsApp.exe')

        elif 'code' in query:
            print(query)
            speak('opening VS code editor')
            os.startfile('C:\\Users\\Altaf khan\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe')

        elif 'play music' in query:
            music_dir = 'C:\\Users\\teach\\Music\\iTunes\\Album Artwork\\Download'
            songs = os.listdir(music_dir)
            speak('i am going to play music')
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'time' in query:
            str_time = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f'the time is {str_time}')

        elif "mail" in query:
            try:
                speak('sending email')
                receiver = 'teacheraltafs@gmail.com'
                message = 'mail transfer by jarvis assistant'
                send_emails(receiver, message)
                speak('email sent')
            except Exception as e:
                print(e)
                speak('sorry i am unable to send')
