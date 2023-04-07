import random
import datetime
import webbrowser
import os
import pyttsx3
import speech_recognition as sr

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Greet the user
def greet():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        engine.say("Morning Sir!")
    elif hour == 5:
        engine.say("Engaging morning Routine")
    elif hour >= 12 and hour < 18:
        engine.say("Good afternoon!")
    else:
        engine.say("Good evening!")
    engine.say("Tasks for the day are ready to be engaged, Good Luck today Sir")
    engine.runAndWait()

# Recognize speech input
def recognize_speech():

    # Implementing Voice Recognizer
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-US')
        print(f"User said: {query}\n")
    except Exception as e:
        print("I'm sorry, I did not understand what you said.")
        return "None"
    return query

# Main function
if __name__ == "__main__":
    greet()
    while True:
        query = recognize_speech().lower()
        if "open youtube" in query:
            webbrowser.open("https://www.youtube.com")
        elif "open google" in query:
            webbrowser.open("https://www.google.com")
        elif "play music" in query:
            music_dir = 'C:\\Music\\'
            songs = os.listdir(music_dir)
            song = random.choice(songs)
            os.startfile(os.path.join(music_dir, song))
        elif "what time is it" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            engine.say(f"The time is {strTime}")
            engine.runAndWait()
        elif "disengage" in query:
            engine.say("disengaging")
            engine.runAndWait()
        elif "list today's task" in query:
            engine.say("Your tasks for today are: 5 Leetcode Problems")
            engine.runAndWait()
            break
        else:
            engine.say("I'm sorry, I did not understand what you said.")
            engine.runAndWait()