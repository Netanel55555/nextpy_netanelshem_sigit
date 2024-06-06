import pyttsx3


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


if __name__ == "__main__":
    sentence = "first time i'm using a package in next.py course"
    speak(sentence)
