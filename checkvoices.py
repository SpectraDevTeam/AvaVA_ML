import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
    print("Voice:", voice.name)
    print("ID:", voice.id)
    print("Path:", engine.getProperty('voice'))