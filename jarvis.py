import pyttsx3 
import speech_recognition as sr
import webbrowser

myVoiceEngine = pyttsx3.init('sapi5')
voices = myVoiceEngine.getProperty('voices')
myVoiceEngine.setProperty('voice', voices[1].id)


def speak(audio):
    myVoiceEngine.say(audio)
    myVoiceEngine.runAndWait()  

def CommandInput():
    recog = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recog.pause_threshold = 1
        audio = recog.listen(source)

    try:
        print("Recognizing...")    
        query = recog.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Didn't Get It Sir")  
        return "None"
    return query

if __name__ == "__main__":
    speak("Hello Sir! Iam Alice Here To Help You")
    while 1:
        query = CommandInput().lower()
        if "wake up" in query:
            speak("Yes Sir iam Awake. How Can I Help You Sir...") 
        elif "talk to" in query:
            myVoiceEngine.setProperty('voice', voices[0].id)
            speak("Yes Sir iam Here. How Can I Help You Sir...")
        elif "like" in query:
             speak("Yes Sir! I like her. She is Kinda Cute")
             myVoiceEngine.setProperty('voice', voices[1].id)
             speak("Shutup Jarvis.. I Have A Boyfriend")
             myVoiceEngine.setProperty('voice', voices[0].id)
             speak("ooops!.... I think its time to play arjit singh sir")
             webbrowser.open("https://www.youtube.com/watch?v=284Ov7ysmfA")
        elif "Kira" in query:
            speak("Kira.. Is A Professional Call Of Duty,valorant and BGMI Player. Kira is also Known As Noxious Beats AKA OOtkarsh")
        else:
            print("No query matched")