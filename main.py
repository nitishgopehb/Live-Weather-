import requests
import json
import win32com.client as wincom
import pyttsx3
converter = pyttsx3.init()
speak = wincom.Dispatch("SAPI.SpVoice")
text = "Python text-to-speech test. using win32com.client"
city = input("Enter the name of the city.\n")
url = f"http://api.weatherapi.com/v1/current.json?key=48cb8a54e632417ca5b164206240711&q={city}"
r = requests.get(url)
wdic=json.loads(r.text)
w=wdic["current"]["temp_c"]
f=wdic["current"]["temp_f"]
text =f"The current weather in {city} is {w} degree celsius and {f} degree Farenheit"
speak.Speak(text)

