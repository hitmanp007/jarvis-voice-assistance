import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import time
import pyautogui

# ---------------- TEXT TO SPEECH SETUP ----------------
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 170)

def speak(audio):
    engine.stop()
    engine.say(audio)
    engine.runAndWait()

# ---------------- WISH FUNCTION ----------------
def wishme():
    hour = datetime.datetime.now().hour

    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am Jarvis. How may I help you?")

# ---------------- TAKE COMMAND ----------------
def takecommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        return query.lower()

    except Exception:
        print("Say that again please...")
        return None

# ---------------- MAIN PROGRAM ----------------
if __name__ == "__main__":
    wishme()

    while True:
        query = takecommand()

        if query is None:
            continue

        # Wikipedia
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        # Open Websites
        elif 'open youtube' in query:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")

        elif 'open google' in query:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")

        elif 'open instagram' in query:
            speak("Opening Instagram")
            webbrowser.open("https://www.instagram.com")

        elif 'open stackoverflow' in query:
            speak("Opening StackOverflow")
            webbrowser.open("https://stackoverflow.com")

        # Play Music
        elif 'play music' in query:
            music_dir = r"C:\Users\pranav\Music"
            songs = [song for song in os.listdir(music_dir) if song.endswith(".mp3")]
            if songs:
                song = random.choice(songs)
                speak("Playing music")
                os.startfile(os.path.join(music_dir, song))
            else:
                speak("No music files found.")

        # Tell Time
        elif 'time' in query:
            now = datetime.datetime.now()
            speak(f"The time is {now.hour} {now.minute}")
            print(now)

        # Tell Date
        elif 'date' in query:
            today = datetime.date.today()
            speak(f"Today's date is {today}")

        # Tell Day
        elif 'day' in query:
            day = datetime.datetime.now().strftime("%A")
            speak(f"Today is {day}")

        # Search Google
        elif 'search' in query:
            speak("What should I search?")
            search_query = takecommand()
            if search_query:
                webbrowser.open(f"https://www.google.com/search?q={search_query}")

        # Take Screenshot
        elif 'screenshot' in query:
            speak("Taking screenshot")
            screenshot = pyautogui.screenshot()
            screenshot.save("screenshot.png")
            speak("Screenshot saved")

        # Tell a Joke
        elif 'joke' in query:
            jokes = [
                "Why do programmers prefer dark mode? Because light attracts bugs.",
                "Why do Java developers wear glasses? Because they don't see sharp.",
                "Why was the computer cold? It forgot to close windows."
            ]
            joke = random.choice(jokes)
            speak(joke)

        # Open VS Code
        elif 'open code' in query:
            codePath = r"C:\Users\pranav\Downloads\VSCodeUserSetup-x64-1.98.2.exe"
            os.startfile(codePath)

        # Exit
        elif 'exit' in query or 'stop' in query:
            speak("Goodbye Pranav. Have a great day!")
            break