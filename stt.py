import speech_recognition as sr

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ Speak...")
        audio = recognizer.listen(source)
    return recognizer.recognize_google(audio, language="en-IN")
