import speech_recognition as sr
import pyttsx3
import platform
import os
from playsound import playsound
import subprocess
import boto3
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing
from tempfile import gettempdir

session = boto3.Session()
polly = session.client("polly")

current_os = platform.system()
print(f"Launching on {current_os}")
if current_os == "Windows":
    idvoice = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
if current_os == "Darwin":
    idvoice = "com.apple.voice.premium.en-UK.Serena"

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', idvoice)
newVoiceRate = 100
engine.setProperty('rate', newVoiceRate)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
     
    r = sr.Recognizer()
     
    with sr.Microphone() as source:
         
        print("Now listening")
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1
        audio = r.listen(source)  
    try:
        query = r.recognize_google(audio, language ='en-US')
    except:
        query = ""
    
    
    return query

def listen_for_wakeup(continuereading):
    r = sr.Recognizer()
    while continuereading == True:
        print("Listening For Wakeup")
        with sr.Microphone() as source:
            audio = r.listen(source)
            try:
                wakeup = r.recognize_google(audio)
                wakeup = wakeup.lower()
                if "sam" in wakeup:
                    return True
                else:
                    return False
            except:
                continue

def speakPolly(input):
    response = polly.synthesize_speech(Text=input, OutputFormat="mp3", VoiceId="Amy")
    with closing(response["AudioStream"]) as stream:
           output = os.path.join(gettempdir(), "speech.mp3")

           try:
            # Open a file for writing the output as a binary stream
                with open(output, "wb") as file:
                   file.write(stream.read())
           except IOError as error:
              # Could not write to file, exit gracefully
              print(error)

    playsound(output)