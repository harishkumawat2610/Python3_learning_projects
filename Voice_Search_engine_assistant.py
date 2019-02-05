import speech_recognition as hk
import webbrowser

r=hk.Recognizer()

with hk.Microphone() as source:
    print("speech which You want to Search on google")
    audio = r.listen(source)

print("opening:"+ r.recognize_google(audio))


target= r.recognize_google(audio)
hk=target.replace(" ","+")
mk=("https://www.google.com/search?q="+hk)
webbrowser.get('firefox').open(hk)
