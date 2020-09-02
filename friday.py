import datetime
import wikipedia
import pyttsx3
import speech_recognition as sr
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("Welcome back sir, I am friday Your personal assistant.")


def takeCommand1():
    """it takes input from user microphone"""
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except Exception as e:
            print(e)
            return "None"
        return query

def takeCommand():
    """it takes input from user microphone"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening ...")
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing ...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except Exception as e:
            print(e)
            return "None"
        return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand1().lower()
        if 'friday' in query:
            speak('Yes sir, How can I help You?')
            query = takeCommand().lower()
            if 'wikipedia' in query:
                speak("Searching Wikipedia ..")
                query = query.replace("wikipedia", "")
                result = wikipedia.summary(query, sentences=2)
                speak('According to wikipedia.')
                print(result)
                speak(result)
            elif 'open google' in query:
                webbrowser.open("Google.com")
            elif 'open geeksforgeeks' in query:
                webbrowser.open("https://www.geeksforgeeks.org/")
            elif 'open stackoverflow' in query:
                webbrowser.open("https://stackoverflow.com/")
            elif 'play music' in query:
                music_dir = 'absolute path of music dir'
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[0]))
            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                print(strTime)
                speak(f"Sir the time is {strTime}")
            elif 'google' in query:
                speak("What to search?")
                sub_query=takeCommand()
                webbrowser.open("http://google.com/search?q="+sub_query)
            elif 'open sublime text' in query:
                pathname='absolute path of Sublime Text'
                os.startfile(pathname)
            elif 'ganna' in query:
                webbrowser.open('https://gaana.com/discover')
            elif 'thank you' in query:
                speak('I am always here for you Sir!')
            elif 'quit' in query:
                speak('Meet you soon sir.')
                exit()
        elif 'thank you' in query:
            speak('first let me do something for you sir')
