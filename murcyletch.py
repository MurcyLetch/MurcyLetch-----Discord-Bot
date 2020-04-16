import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")
    elif hour>=12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("hi!.......... its mucyletch....... you are just fantastic.............................how can i help you???")       
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold=1
        audio = r.listen(source)
    try:
        print("recognizing..........")
        query = r.recognize_google(audio)
        print(f"User Said:{query}\n")
    except Exception:
        print("Say that again Please.....")
        return "None"
    return query           

             
if __name__ =="__main__":
    wishme() 
    if 1:
        query=takecommand().lower()
        if 'wikipedia' in query:
            speak("searching wikipedia")
            query=query.replace('wikipedia','')
            result=wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            print(result)
            speak(result)
        elif 'youtube'in query:
            webbrowser.open("youtube.com") 
        elif 'google' in query:
            webbrowser.open("google.com") 
        elif 'github' in query:
            webbrowser.open("github.com")
        elif 'linked in' in query:
            webbrowser.open("linked in.com")
        #latest singer's songs................    
        elif 'arijit singh song'in query:
            webbrowser.open("https://www.youtube.com/watch?v=Hzmp3z6deF8") 
        elif 'atif aslam song'in query:
            webbrowser.open("https://www.youtube.com/watch?v=R9PHzAR4G3g")    
        elif 'kumar shanu song'in query:
            webbrowser.open("https://www.youtube.com/watch?v=6-emBDTy4-E")
        elif 'rahat fateh ali khan song'in query:
            webbrowser.open("https://www.youtube.com/watch?v=k6FthKxWObU") 
        elif 'udit narayan song'in query:
            webbrowser.open("https://www.youtube.com/watch?v=R_4GBP3Jsyw") 
        elif 'sonu nigam song'in query:
            webbrowser.open("https://www.youtube.com/watch?v=k0beSq9pkbA") 
        elif 'alka yagnik songs'in query:
            webbrowser.open("https://www.youtube.com/watch?v=FgBu2c7uBqw")       
        elif 'neha kakkar'in query:
            webbrowser.open("https://www.youtube.com/watch?v=6iDEs__smVw")    
        elif 'shreya ghoshal song'in query:
            webbrowser.open("https://www.youtube.com/watch?v=bqsUEPRKQG0")     
        #search others in you tube.....by entering youtube.......... 
        #ask about time
        elif 'the time' in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir,  the time is{strtime}")
        #open apps in your system    
        elif 'open visual studio code' in query:
            c1path="C:\\Users\\LENOVO\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(c1path)
        elif 'open pycharm' in query:
            c2path="C:\\Program Files\\JetBrains\\PyCharm Community Edition 2019.1.3\\bin\\pycharm64.exe"  
            os.startfile(c2path)
        elif 'open anaconda' in query:
            c3path="C:\\Users\\LENOVO\\Anaconda3\\pythonw.exe C:\\Users\\LENOVO\Anaconda3\\cwp.py C:\\Users\\LENOVO\\Anaconda3 C:\\Users\\LENOVO\\Anaconda3\\pythonw.exe C:\\Users\\LENOVO\\Anaconda3\\Scripts\\anaconda-navigator-script.py" 
            os.startfile(c3path)  
        elif '*' in query:
            speak("you should not say this...............behave yourself!!.........otherwise i will not talk to you ")  
        elif 'thank' in query:
            speak("you are welcome dear...................i love you")      

